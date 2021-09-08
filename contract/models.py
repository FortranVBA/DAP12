from django.db import models
from client.models import Client


# Create your models here.
class ContractStatut(models.Model):
    """ContractStatut model."""

    Name = models.CharField(max_length=25)


class Contract(models.Model):
    """Contract model."""

    ClientID = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateUpdated = models.DateTimeField(auto_now=True)
    Amount = models.FloatField()
    PaymentDue = models.DateTimeField()
    ContractStatutID = models.ForeignKey(to=ContractStatut, on_delete=models.CASCADE)

    def get_staff_contact(self):
        return [self.ClientID.SalesContactID]
