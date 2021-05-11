from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class User(AbstractUser):
    friends = models.ManyToManyField('self', through='Friendship')


class Friendship(models.Model):
    from_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    accepted_status = models.BooleanField(blank=True, null=True)
