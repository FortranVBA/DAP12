"""Project OC DAP 12 - Account serializers file."""

from account.models import Staff
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class StaffSerializer(serializers.ModelSerializer):
    """Staff serializer."""

    class Meta:
        """Serializer meta properties."""

        model = Staff
        fields = ["id", "username", 'password', 'StaffProfileID']

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)