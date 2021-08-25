"""Project OC DAP 12 - Account serializers file."""

from account.models import Staff
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer used for registration."""

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    class Meta:
        """Serializer meta properties."""

        model = Staff
        fields = ("username", "password")

    def create(self, validated_data):
        """Register a person as user."""
        staff = Staff.objects.create(
            username=validated_data["username"],
        )

        staff.set_password(validated_data["password"])
        staff.save()

        return staff


class StaffSerializer(serializers.ModelSerializer):
    """Staff serializer."""

    class Meta:
        """Serializer meta properties."""

        model = Staff
        fields = ["id", "username"]