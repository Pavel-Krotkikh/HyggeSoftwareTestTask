from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from users.serializers import UserDetailSerializer


@api_view(['POST'])
def auth_register(request):
    serializer = UserDetailSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    User.objects.create_user(request.data['username'],
                            request.data['email'],
                            request.data['password'])

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def auth_login(request):
    serializer = UserDetailSerializer(data=request.data)

    user = authenticate(
        username=serializer.data['username'],
        password=serializer.data['password'],
    )

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def auth_logout(request):
    logout(request.user)
    return True
