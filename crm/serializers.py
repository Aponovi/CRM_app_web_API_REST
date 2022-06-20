from rest_framework import request
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.generics import get_object_or_404

from crm.models import Client, Contract, Event


class ClientsListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id',
                  'first_name',
                  'last_name',
                  'company_name',
                  ]
        read_only_fields = ['date_created',
                            'date_update',
                            ]


class ClientDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id',
                  'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'mobile',
                  'company_name',
                  'sales_contact',
                  ]
        read_only_fields = ['date_created',
                            'date_update',
                            ]


class ContractsListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id',
                  "client",
                  "status",
                  "sales_contact",
                  ]
        read_only_fields = ['date_created',
                            'date_update',
                            ]


class ContractDetailSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id',
                  "client",
                  "status",
                  "amount",
                  "payement_due",
                  "sales_contact",
                  ]
        read_only_fields = ['created_time',
                            'updated_time',
                            ]


class EventsListSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id',
                  'status',
                  'event_date',
                  'support_contact',
                  ]


class EventDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id',
                  'contract',
                  'attendees',
                  'event_date',
                  'notes',
                  'support_contact',
                  ]

        read_only_fields = ['created_time',
                            'updated_time',
                            ]
