from django.db import models
from django.contrib.auth.models import User
from MetaData.models import Designation


class TeamMemberDetails(models.Model):
    members = models.ManyToManyField(User,related_name='TeamMembers')
    joined_at = models.DateTimeField(auto_now_add=True)
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE)

    def __str__(self):
        return self.members.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ForeignKey(TeamMemberDetails,on_delete=models.CASCADE)
    teamRequests = models.ManyToManyField(User,related_name='TeamRequests')

    def __str__(self):
        return self.name


class ProjectNerve(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    bids = models.ManyToManyField(User,related_name='ProjectRequests')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
