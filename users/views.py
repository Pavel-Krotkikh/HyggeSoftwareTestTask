from django.contrib.auth import authenticate, logout
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User, Friendship
from users.serializers import UserDetailSerializer, UserSetFriendSerializer, UsersListSerializer


@api_view(['POST'])
def user_register(request):
    serializer = UserDetailSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    User.objects.create_user(request.data['username'],
                            request.data['email'],
                            request.data['password'])

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def user_auth(request):
    serializer = UserDetailSerializer(data=request.data)

    user = authenticate(
        username=serializer.data['username'],
        password=serializer.data['password'],
    )

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def user_logout(request):
    logout(request.user)
    return True


@api_view(['GET'])
def user_list(request):
    all_users = User.objects.all()
    serializer = UserDetailSerializer(all_users, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def user_detail(request):
    user = request.user
    serializer = UserDetailSerializer(user)

    return Response(serializer.data)


@api_view(['POST'])
def friend_request(request, user_id):
    auth_user = request.user
    another_user = User.objects.filter(id=user_id).first()
    auth_user.friends.add(another_user)

    serializer = UserDetailSerializer(another_user)

    return Response(serializer.data)


@api_view(['POST'])
def friend_accept(request, user_id):
    to_user_id = user_id
    status_to_change = request.data['status']

    from_user = request.user
    to_friend_info = Friendship.objects.filter(
        to_user=to_user_id,
        from_user=from_user.id).first()

    if not to_friend_info:
        raise Exception("Нет такого друга пока что!")

    from_friend_info = Friendship.objects.filter(
        to_user=from_user.id,
        from_user=to_user_id).first()

    to_friend_info.accepted_status = status_to_change
    to_friend_info.save()

    from_friend_info.accepted_status = status_to_change
    from_friend_info.save()

    return Response(True)


@api_view(['GET'])
def friends(request):
    # Нужен запрос на получение друзей только тех,
    # у кого подтвержденный статус дружбы

    user = request.user
    # user_friends = User.objects.filter(id=user.id).friends.filter(accepted_status=True).all()
    # user_friends = User.objects.filter(
    #     friendship__accepted_status=True,
    #
    # ).all()

    serializer = UsersListSerializer(user.friends, many=True)
    return Response(serializer.data)
