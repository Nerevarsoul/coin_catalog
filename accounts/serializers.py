from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User


class OAuth2InputSerializer(serializers.Serializer):

    provider = serializers.CharField(required=False)
    code = serializers.CharField()
    redirect_uri = serializers.CharField(required=False)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ('is_staff', 'is_active', 'date_joined', 'password',
                   'last_login', 'user_permissions', 'groups', 'is_superuser',)


class TokenSerializer(serializers.Serializer):

    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key


class UserTokenSerializer(TokenSerializer, UserSerializer):
    pass
