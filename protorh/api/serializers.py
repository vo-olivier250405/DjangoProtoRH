from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    firstname = serializers.CharField(max_length=1000, required=True)
    email = serializers.CharField(max_length=1000, required=True)
