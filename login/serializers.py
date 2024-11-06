from rest_framework import serializers

from .models import CustomUser


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "password")
