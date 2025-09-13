from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'date_joined')
    search_fields = ('username', 'email', 'phone')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'address', 'profile_picture', 'terms_accepted')}),
    )