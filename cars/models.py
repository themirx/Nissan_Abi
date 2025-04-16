from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('شماره موبایل الزامی است')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)

class User(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='شماره موبایل')
    is_verified = models.BooleanField(default=False, verbose_name='تایید شده')
    verification_code = models.CharField(max_length=6, null=True, blank=True, verbose_name='کد تایید')
    verification_code_expiry = models.DateTimeField(null=True, blank=True, verbose_name='انقضای کد تایید')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.phone_number

class Car(models.Model):
    TYPE_CHOICES = [
        ('sedan', 'سدان'),
        ('coupe', 'کوپه'),
        ('suv', 'شاسی بلند'),
        ('sport', 'اسپرت'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='نام خودرو')
    model = models.CharField(max_length=100, verbose_name='مدل')
    year = models.IntegerField(verbose_name='سال تولید')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='قیمت')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='cars/', verbose_name='تصویر')
    engine = models.CharField(max_length=100, verbose_name='موتور')
    transmission = models.CharField(max_length=100, verbose_name='گیربکس')
    fuel_type = models.CharField(max_length=50, verbose_name='نوع سوخت')
    color = models.CharField(max_length=50, verbose_name='رنگ')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='sedan', verbose_name='نوع خودرو')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'خودرو'
        verbose_name_plural = 'خودروها'

    def __str__(self):
        return f"{self.name} - {self.model} ({self.year})"

class Tire(models.Model):
    BRAND_CHOICES = [
        ('michelin', 'میشلن'),
        ('bridgestone', 'بریجستون'),
        ('continental', 'کنتیننتال'),
        ('pirelli', 'پیرلی'),
        ('goodyear', 'گودیر'),
        ('dunlop', 'دانلوپ'),
        ('yokohama', 'یوکوهاما'),
        ('hankook', 'هانکوک'),
        ('nokian', 'نوکیان'),
        ('kavir', 'کویر تایر'),
        ('yazd', 'یزد تایر'),
        
    ]

    SEASON_CHOICES = [
        ('summer', 'تابستانی'),
        ('winter', 'زمستانی'),
        ('all_season', 'چهار فصل'),
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, verbose_name='برند')
    model = models.CharField(max_length=100, verbose_name='مدل')
    size = models.CharField(max_length=20, verbose_name='سایز')
    season = models.CharField(max_length=20, choices=SEASON_CHOICES, verbose_name='فصل')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='قیمت')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='tires/', verbose_name='تصویر')
    stock = models.PositiveIntegerField(default=0, verbose_name='موجودی')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'لاستیک'
        verbose_name_plural = 'لاستیک‌ها'

    def __str__(self):
        return f"{self.get_brand_display()} {self.model} - {self.size}"

class Contact(models.Model):
    address = models.TextField(verbose_name='آدرس')
    working_hours = models.CharField(max_length=200, verbose_name='ساعات کاری')
    phone = models.CharField(max_length=20, verbose_name='شماره تماس', default='118')
    email = models.EmailField(verbose_name='ایمیل')
    instagram = models.URLField(blank=True, null=True, verbose_name='اینستاگرام')
    telegram = models.URLField(blank=True, null=True, verbose_name='تلگرام')
    whatsapp = models.URLField(blank=True, null=True, verbose_name='واتساپ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'اطلاعات تماس'
        verbose_name_plural = 'اطلاعات تماس'

    def __str__(self):
        return 'اطلاعات تماس'
