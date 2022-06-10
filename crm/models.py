from django.conf import settings
from django.db import models


class Client(models.Model):

    STATUS_CHOICES = (
        ("prospect", "prospect"),
        ("client", "client"),
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    company_name = models.TextField(max_length=250)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='prospect')
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['company_name']

    def __str__(self):
        return f"{self.pk} - {self.company_name} - {self.first_name} {self.last_name}"


class Contract(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="contracts")
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payement_due = models.DateField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"({self.client})"


class Event(models.Model):

    STATUS_CHOICES = (
        ("coming", "coming"),
        ("finished", "finished"),
        ("cancel", "cancel"),
    )

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="event_contract")
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default='coming')
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="events_support")

    def __str__(self):
        return f"({self.pk}) {self.event_date}"
