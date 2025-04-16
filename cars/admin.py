from django.contrib import admin
from .models import Car, User, Tire, Contact

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'year', 'price', 'type', 'created_at')
    search_fields = ('name', 'model')
    list_filter = ('year', 'fuel_type', 'type')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'is_verified', 'is_staff')
    search_fields = ('phone_number',)
    list_filter = ('is_verified', 'is_staff')

@admin.register(Tire)
class TireAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'size', 'season', 'price', 'stock')
    search_fields = ('brand', 'model', 'size')
    list_filter = ('brand', 'season')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'created_at')
    search_fields = ('address', 'phone', 'email')
    readonly_fields = ('created_at', 'updated_at')
