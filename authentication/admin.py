from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUser(UserAdmin):
    list_display = ('username', 'get_groups')
    search_fields = ('username',)
    list_filter = ('groups',)

    @staticmethod
    def get_groups(obj):
        return obj.groups.values_list('name', flat=True).first()


admin.site.register(User, CustomUser)
