from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, request, filters
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from crm.models import Client, Contract, Event
from crm.permissions import IsSalesTeam, IsSupportTeam
from crm.serializers import ClientsListSerializer, ClientDetailSerializer, \
    ContractsListSerializer, ContractDetailSerializer, \
    EventsListSerializer, EventDetailSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientsListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [IsSalesTeam | IsSupportTeam]
    filter_fields = ['name', 'email']
    queryset = Client.objects.all()
    filterset_fields = ['last_name',
                        'email',
                        ]

    def get_serializer_class(self):
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class ContractViewSet(ModelViewSet):
    serializer_class = ContractsListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsSalesTeam | IsSupportTeam]
    queryset = Contract.objects.all()
    filterset_fields = {'client__last_name': ['exact'],
                        'client__email': ['exact'],
                        'created_time': ['gte', 'lte', 'exact', 'gt', 'lt'],
                        'amount': ['exact'],
                        }

    def get_serializer_class(self):
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        client = get_object_or_404(Client, pk=self.request.data['client'])
        client.status = 'client'
        client.save()
        serializer.save(sales_contact=self.request.user)


class EventViewSet(ModelViewSet):
    serializer_class = EventsListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [IsSalesTeam | IsSupportTeam]
    queryset = Event.objects.all()
    filterset_fields = ['contract__client',
                        'contract_id',
                        'event_date',
                        ]

    def get_serializer_class(self):
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()
