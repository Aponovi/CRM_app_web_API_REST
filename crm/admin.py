from django.contrib import admin
from crm.models import Client, Contract, Event


class CustomClient(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'first_name', 'last_name', 'status')
    search_fields = ('company_name', 'last_name',)
    list_filter = ('status',)


class CustomContract(admin.ModelAdmin):
    list_display = ('id', 'client', 'sales_contact', 'status')
    search_fields = ('id', 'client', 'sales_contact')
    list_filter = ('status',)


class CustomEvent(admin.ModelAdmin):
    list_display = ('id', 'contract', 'status', 'event_date', 'support_contact')
    search_fields = ('id', 'contract', 'support_contact')
    list_filter = ('status', 'event_date', 'support_contact')




admin.site.register(Client, CustomClient)
admin.site.register(Contract, CustomContract)
admin.site.register(Event, CustomEvent)

# @admin.action(description='Mark selected stories as published')
# def make_published(modeladmin, request, queryset):
#     queryset.update(status='p')
