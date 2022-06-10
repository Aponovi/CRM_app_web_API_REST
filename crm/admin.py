from django.contrib import admin
from crm.models import Client, Contract, Event


admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)


# @admin.action(description='Mark selected stories as published')
# def make_published(modeladmin, request, queryset):
#     queryset.update(status='p')