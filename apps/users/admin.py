from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model



class CustomUserAdmin(UserAdmin):
    model = get_user_model()
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('photo', "bio", "location",)}),
    )


admin.site.register(User, CustomUserAdmin)
