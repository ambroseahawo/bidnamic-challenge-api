from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        # password protection - when you GET users, the password field to be omitted
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    # hash password
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # create auth-token for each user
        Token.objects.create(user=user)
        return user
