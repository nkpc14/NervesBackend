from django.db import models


class UserProfileVerification(models.Model):
    aadhar = models.IntegerField(null=True, blank=True)
    aadharPhoto = models.ImageField(null=True, blank=True)
    panCard = models.CharField(max_length=12, null=True, blank=True)
    panCardPhoto = models.ImageField(null=True, blank=True)
    otherIdProof = models.CharField(max_length=16, null=True, blank=True)
    otherIdProofImage = models.ImageField(null=True, blank=True)


class OTP(models.Model):
    otp = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
