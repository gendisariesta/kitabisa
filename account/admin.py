from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name','location')}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name','location', 'is_staff', 'is_superuser')}),
    )
admin.site.register(User, CustomUserAdmin)