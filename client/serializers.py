"""Project OC DAP 12 - Client models file."""

from .models import Client
from rest_framework import serializers

# Create your models here.


class ClientSerializer(serializers.ModelSerializer):
    """Client serializer."""

    class Meta:
        """Serializer meta properties."""

        model = Client
        fields = [
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

        extra_kwargs = {
            "SalesContactID": {"required": False},
            "ClientStatutID": {"required": False},
        }


    def create(self, validated_data):
        """Create client."""
        #validated_data["SalesContactID"] = 
        #validated_data["ClientStatutID"] = 

        return super().create(validated_data)