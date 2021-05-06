from rest_framework import serializers
from users.models import User


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email')


class UserSetFriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'id'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
