from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    firstname = serializers.CharField(max_length=1000, required=True)
    email = serializers.EmailField(max_length=1000, required=True)

    class Meta:
        model = User
        fields = ("id", "firstname", "email")

    def create(self, validated_data):
        """_summary_

        Args:
            validated_data (_type_): _description_
        """
        return User.objects.create(
            firstname=validated_data.get("firstname"),
            email=validated_data.get("email")
        )

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get(
            "firstname", instance.firstname)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
