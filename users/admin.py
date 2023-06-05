from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'discord_id', 'email', 'is_staff']
    pass


admin.site.register(User, CustomUserAdmin)