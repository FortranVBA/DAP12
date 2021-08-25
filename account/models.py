from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


#class StaffProfile(models.Model):
#   """ClientStatut model."""

#   Name = models.CharField(max_length=25)


class Staff(AbstractUser):
    """Staff model."""
    #StaffProfileID = models.ForeignKey(to=StaffProfile, on_delete=models.CASCADE)
