"""Project OC DAP 12 - Contract models file."""

from .models import Contract
from rest_framework import serializers

# Create your models here.

class ContractSerializer(serializers.ModelSerializer):
    """Contract serializer."""

    class Meta:
        """Serializer meta properties."""

        model = Contract
        fields = [
            "pk",
            "ClientID",
            "DateCreated",
            "DateUpdated",
            "Amount",
            "PaymentDue",
            "ContractStatutID",
        ]
