from django.db import models
from django.contrib.auth.models import User
from Verification.models import UserProfileVerification, OTP
from MetaData.models import State,UserProfileType
from django_countries.fields import CountryField


class UserAuthentication(User):
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=512, null=True)
    mobile = models.IntegerField(null=True)
    bio = models.CharField(max_length=255, null=True)
    profile_photo = models.ImageField(null=True, blank=True)
    cover_photo = models.ImageField(null=True, blank=True)
    linkedIn = models.URLField(max_length=255, blank=True, null=True)
    github = models.URLField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)
    gmail = models.EmailField(null=True)
    pincode = models.IntegerField(null=True)
    verification = models.OneToOneField(UserProfileVerification, on_delete=models.CASCADE, null=True)
    country = CountryField(null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    profile_type = models.ForeignKey(UserProfileType,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




class NodeStates(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class NodeOperations(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
