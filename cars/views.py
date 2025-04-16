from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Car, User, Tire, Contact

def home(request):
    latest_cars = Car.objects.all().order_by('-created_at')[:3]
    return render(request, 'cars/home.html', {'latest_cars': latest_cars})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

def login_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            user = User.objects.create(phone_number=phone_number)
            
        # تولید کد تایید
        code = '123456'  # کد ثابت برای تست
        user.verification_code = code
        user.verification_code_expiry = timezone.now() + timedelta(minutes=5)
        user.save()
        
        messages.success(request, f'کد تایید: {code}')
        return redirect('cars:verify')
            
    return render(request, 'cars/login.html')

def verify_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        phone_number = request.POST.get('phone_number')
        
        try:
            user = User.objects.get(phone_number=phone_number)
            if user.verification_code == code and user.verification_code_expiry > timezone.now():
                user.is_verified = True
                user.save()
                login(request, user)
                messages.success(request, 'ورود با موفقیت انجام شد.')
                return redirect('cars:home')
            else:
                messages.error(request, 'کد تایید نامعتبر یا منقضی شده است.')
        except User.DoesNotExist:
            messages.error(request, 'کاربری با این شماره موبایل یافت نشد.')
            
    return render(request, 'cars/verify.html')

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'خروج با موفقیت انجام شد.')
    return redirect('cars:home')

def tire_list(request):
    tires = Tire.objects.all()
    return render(request, 'cars/tire_list.html', {'tires': tires})

def tire_detail(request, tire_id):
    tire = Tire.objects.get(id=tire_id)
    return render(request, 'cars/tire_detail.html', {'tire': tire})

def sedan_list(request):
    sedans = Car.objects.filter(type='sedan').order_by('-created_at')
    return render(request, 'cars/sedan_list.html', {'sedans': sedans})

def coupe_list(request):
    coupes = Car.objects.filter(type='coupe').order_by('-created_at')
    return render(request, 'cars/coupe_list.html', {'coupes': coupes})

def car_search(request):
    query = request.GET.get('q', '')
    type_filter = request.GET.get('type', '')
    year_filter = request.GET.get('year', '')
    
    cars = Car.objects.all()
    
    if query:
        cars = cars.filter(name__icontains=query) | cars.filter(model__icontains=query)
    
    if type_filter:
        cars = cars.filter(type=type_filter)
        
    if year_filter:
        cars = cars.filter(year=year_filter)
        
    years = Car.objects.values_list('year', flat=True).distinct().order_by('-year')
    
    context = {
        'cars': cars,
        'query': query,
        'type_filter': type_filter,
        'year_filter': year_filter,
        'years': years,
        'types': Car.TYPE_CHOICES,
    }
    
    return render(request, 'cars/car_search.html', context)

def contact(request):
    contact_info = Contact.objects.first()
    return render(request, 'cars/contact.html', {'contact': contact_info})
