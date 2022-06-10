from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUser(admin.ModelAdmin):
    model = User
    list_display = ('username', 'role')
    search_fields = ('username',)
    list_filter = ('groups',)


admin.site.register(User, UserAdmin)
