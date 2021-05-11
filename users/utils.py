from users.models import Friendship


def friend_accept_util(from_user, to_user_id, status_to_change):

    to_friend_info = Friendship.objects.filter(
        to_user=to_user_id,
        from_user=from_user.id).first()

    if not to_friend_info:
        raise Exception("Friend does not exist yet!")

    from_friend_info = Friendship.objects.filter(
        to_user=from_user.id,
        from_user=to_user_id).first()

    to_friend_info.accepted_status = status_to_change
    to_friend_info.save()

    from_friend_info.accepted_status = status_to_change
    from_friend_info.save()
