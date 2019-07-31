from django.db import models
from django.contrib.auth.models import User


class PermissionModel(models.Model):
    permissions = models.IntegerField(choices=(
        (1, "Allow Global Access"),
        (2, "Read"),
        (3, "Comment"),
        (4, "Share"),
    ), default=1)


class NervesPermission(models.Model):
    name = models.CharField(max_length=255)
    permissionList = models.ManyToManyField(PermissionModel,related_name='Permissions')


class UserCreatedNerve(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='NerveMembers')

