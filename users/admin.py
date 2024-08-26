from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class UserAdmin(UserAdmin):
    list_display = ('id', 'name', 'username', 'email' , 'is_staff')
    
    fieldsets = UserAdmin.fieldsets + (  # Include 'gender' in the 'Personal Information' section
        ('Other Information', {
            'fields': ('is_email_verified',),
        }),
    )
admin.site.register(User, UserAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'email')
admin.site.register(UserProfile, UserProfileAdmin)

class Contact_Us_Admin(admin.ModelAdmin):
    list_display = ('id','name' , 'subject' , 'email' , 'message')
admin.site.register(ContactUs , Contact_Us_Admin)