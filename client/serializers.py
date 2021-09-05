"""Project OC DAP 12 - Client serializer file."""

from .models import Client
from account.models import Staff
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

    def validate(self, data):
        if 'SalesContactID' in data:
            staff = data['SalesContactID']

            if staff.StaffProfileID.Name != "Vente":
                raise serializers.ValidationError("SalesContactID must be from the Sales"
                " team.")

        return super().validate(data)
