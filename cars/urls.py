from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/<int:pk>/', views.car_detail, name='car_detail'),
    path('login/', views.login_view, name='login'),
    path('verify/', views.verify_code, name='verify'),
    path('logout/', views.logout_view, name='logout'),
    path('tires/', views.tire_list, name='tire_list'),
    path('tires/<int:tire_id>/', views.tire_detail, name='tire_detail'),
    path('sedan/', views.sedan_list, name='sedan_list'),
    path('coupe/', views.coupe_list, name='coupe_list'),
    path('search/', views.car_search, name='car_search'),
    path('contact/', views.contact, name='contact'),
] 