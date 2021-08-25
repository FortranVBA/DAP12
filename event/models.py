from django.db import models
from contract.models import Contract
from account.models import Staff


# Create your models here.
class EventStatut(models.Model):
    """ContractStatut model."""

    Name = models.CharField(max_length=25)


class Event(models.Model):
    """Contract model."""

    ContractID = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateUpdated = models.DateTimeField(auto_now=True)
    Attendees = models.IntegerField()
    EventDate = models.DateTimeField()
    Notes = models.TextField(max_length=8192, blank=True)
    SupportContactID = models.ForeignKey(to=Staff, on_delete=models.CASCADE)
    EventStatutID = models.ForeignKey(to=EventStatut, on_delete=models.CASCADE)
