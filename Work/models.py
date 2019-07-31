from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class Organization(models.Model):
    name = models.CharField(max_length=255)
    admin = models.ForeignKey(User,on_delete=models.CASCADE,related_name='admin',default=0)
    address = models.CharField(max_length=512)
    country = CountryField()
    members = models.ManyToManyField(User,related_name='member')
    created_at = models.DateTimeField(auto_now=True)
