from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('Manager', 'Manager'),
        ('Seller', 'Seller'),
        ('Support', 'Support')
    )

    role = models.CharField(max_length=16, choices=ROLE_CHOICES, null=False, verbose_name='role')

    def __str__(self):
        return f"User: {self.username} | Role: {self.role}"
