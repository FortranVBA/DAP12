from django.db import models
from account.models import Staff


# Create your models here.
class ContractStatut(models.Model):
    """ContractStatut model."""

    Name = models.CharField(max_length=25)


class Contract(models.Model):
    """Contract model."""

    ClientID = models.ForeignKey(to=Staff, on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateUpdated = models.DateTimeField(auto_now=True)
    Amount = models.FloatField()
    PaymentDue = models.DateTimeField()
    ContractStatutID = models.ForeignKey(to=ContractStatut, on_delete=models.CASCADE)
