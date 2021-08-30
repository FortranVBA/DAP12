"""Project OC DAP 12 - Event serializer file."""

from .models import Event
from rest_framework import serializers

# Create your models here.


class EventSerializer(serializers.ModelSerializer):
    """Contract serializer."""

    class Meta:
        """Serializer meta properties."""

        model = Event
        fields = [
            "pk",
            "ContractID",
            "DateCreated",
            "DateUpdated",
            "Attendees",
            "EventDate",
            "Notes",
            "SupportContactID",
            "EventStatutID"
        ]

