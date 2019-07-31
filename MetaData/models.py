from django.db import models


class State(models.Model):
    name = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=25,null=True)
    Image = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    followerCount = models.IntegerField(default=0)
    tagType = models.IntegerField( choices=(
        (1, "People"),
        (2, "Group"),
        (3, "Community"),
        (4, "Nerve"),
    ), default=1)

    def __str__(self):
        return self.name


class Designation(models.Model):
    name = models.CharField(max_length=100)


class UserProfileType(models.Model):
    name = models.CharField(max_length=255)
