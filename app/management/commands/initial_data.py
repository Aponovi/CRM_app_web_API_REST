from django.contrib.auth.models import Permission, Group
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Command(BaseCommand):
    help = 'Create initial data'

    def handle(self, *args, **options):
        UserModel.objects.create_superuser('admin', email='admin@admin.admin', password='admin',
                                           first_name='Ruby', last_name='RHOD')

        add_client = Permission.objects.get(codename='add_client')
        change_client = Permission.objects.get(codename='change_client')
        view_client = Permission.objects.get(codename='view_client')

        add_contract = Permission.objects.get(codename='add_contract')
        change_contract = Permission.objects.get(codename='change_contract')
        view_contract = Permission.objects.get(codename='view_contract')

        add_event = Permission.objects.get(codename='add_event')
        change_event = Permission.objects.get(codename='change_event')
        view_event = Permission.objects.get(codename='view_event')

        sellers_permissions = [
            add_client,
            change_client,
            view_client,
            add_contract,
            change_contract,
            view_contract,
            add_event,
            change_event,
            view_event
        ]

        supports_permissions = [
            view_client,
            view_contract,
            change_event,
            view_event,
        ]

        sellers = Group(name='Sellers')
        sellers.save()
        sellers.permissions.set(sellers_permissions)

        supports = Group(name='Supports')
        supports.save()
        supports.permissions.set(supports_permissions)

        UserModel.objects.create_user('Ben', password='BenBen', groups=sellers)
        UserModel.objects.create_user('Tom', password='TomTom', groups=sellers)
        UserModel.objects.create_user('Nana', password='NanaNana', groups=supports)

        self.stdout.write(self.style.SUCCESS('Data created'))
