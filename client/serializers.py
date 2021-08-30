"""Project OC DAP 12 - Client serializer file."""

from .models import Client
from rest_framework import serializers

# Create your models here.


class ClientSerializer(serializers.ModelSerializer):
    """Client serializer."""

    class Meta:
        """Serializer meta properties."""

        model = Client
        fields = [
            "pk",
            "FirstName",
            "LastName",
            "Email",
            "Phone",
            "Mobile",
            "CompanyName",
            "DateCreated",
            "DateUpdated",
            "SalesContactID",
            "ClientStatutID",
        ]
