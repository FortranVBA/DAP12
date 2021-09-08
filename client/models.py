from django.db import models
from account.models import Staff

# Create your models here.


class ClientStatut(models.Model):
    """ClientStatut model."""

    Name = models.CharField(max_length=25)


class Client(models.Model):
    """Client model."""

    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=20)
    CompanyName = models.CharField(max_length=250)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateUpdated = models.DateTimeField(auto_now=True)
    SalesContactID = models.ForeignKey(to=Staff, on_delete=models.CASCADE)
    ClientStatutID = models.ForeignKey(to=ClientStatut, on_delete=models.CASCADE)

    def get_staff_contact(self):
        return [self.SalesContactID]
