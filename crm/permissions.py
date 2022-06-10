from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import SAFE_METHODS

from crm.models import Client, Contract

owner_methods = ['PUT', 'PATCH']


class IsManagerTeam(permissions.BasePermission):
    # Managers are allowed to use every method
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and request.user.role == 'manager'

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user.is_authenticated and request.user.role == 'manager'


class IsSalesTeam(permissions.BasePermission):
    # Sellers are allowed to use SAFE_METHODS
    # Sellers are allowed to create new clients
    # Sellers are allowed to create contracts for their own client
    # Sellers are allowed to create events for their own client
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and request.user.role == 'seller'

        if request.data.get('contract') and request.data.get('client') is None:
            contract = (get_object_or_404(Contract, pk=request.data.get('contract')))
            client = (get_object_or_404(Client, pk=contract.client.pk))
            return request.user == client.sales_contact
        elif request.data.get('client'):
            client = (get_object_or_404(Client, pk=request.data.get("client")))
            return request.user == client.sales_contact
        return request.user.is_authenticated and request.user.role == 'seller'

    # Sellers are allowed to use UPDATE and PATCH methods only for their own clients
    # Sellers cannot DELETE anything
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and request.user.role == 'seller'
        if request.method in owner_methods:
            return request.user == obj.sales_contact


class IsSupportTeam(permissions.BasePermission):
    # Supports are only allowed to use SAFE_METHODS
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and request.user.role == 'support'

    # Supports is allowed to UPDATE and PATCH only events of their own
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated and request.user.role == 'support'
        if request.method in owner_methods:
            if obj == 'Event':
                return request.user == obj.support_contact
