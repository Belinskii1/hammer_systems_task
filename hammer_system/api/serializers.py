from rest_framework import serializers

from api.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username',)
        model = User