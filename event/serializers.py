"""Project OC DAP 12 - Event serializer file."""

from .models import Event
from rest_framework import serializers

# Create your models here.

class EventSerializer(serializers.ModelSerializer):
    """Event serializer."""

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

    def validate(self, data):
        """Validate fields."""

        if 'SupportContactID' in data:
            staff = data['SupportContactID']

            if staff.StaffProfileID.Name != "Support":
                raise serializers.ValidationError("SupportContactID must be from the"
                " support team.")

        return super().validate(data)
