from rest_framework import serializers

from api.models import User, ActivationCode



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username',)
        model = User


class TokenSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'telephone_number'
        )
