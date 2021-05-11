from django.contrib.auth import authenticate, logout
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User, Friendship
from users.serializers import UserDetailSerializer, UsersListSerializer, \
    UserFriendRequestSerializer
from users.utils import friend_accept_util


@api_view(['GET'])
def user_list(request):
    all_users = User.objects.all()
    serializer = UsersListSerializer(all_users, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def user_me(request):
    user = request.user
    serializer = UserDetailSerializer(user)

    return Response(serializer.data)


@api_view(['POST'])
def friend_request(request, user_id):
    auth_user = request.user
    another_user = User.objects.filter(id=user_id).first()
    auth_user.friends.add(another_user)

    serializer = UserFriendRequestSerializer(another_user)

    return Response(serializer.data)


@api_view(['POST'])
def friend_accept(request, user_id):
    to_user_id = user_id
    from_user = request.user
    status_to_change = request.data['status']

    friend_accept_util(from_user, to_user_id, status_to_change)

    return Response(True)


@api_view(['GET'])
def friends(request):
    # Нужен запрос на получение друзей только тех,
    # у кого подтвержденный статус дружбы

    # user_friends = User.objects.filter(id=user.id).friends.filter(accepted_status=True).all()
    # user_friends = User.objects.filter(
    #     friendship__accepted_status=True,
    # ).all()

    user = request.user

    serializer = UsersListSerializer(user.friends, many=True)
    return Response(serializer.data)
