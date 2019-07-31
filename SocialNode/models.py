from django.db import models
from django.contrib.auth.models import User
from Automation.models import PostAutomation


class Like(models.Model):
    likedBy = models.OneToOneField(User, on_delete=models.CASCADE)
    emoji = models.ImageField(null=True)
    likeType = models.IntegerField(choices=(
        (1, "Heart"),
        (2, "Laugh"),
        (3, "ThumbsUp"),
        (4, "Nerve"),
    ), default=1)

    def __str__(self):
        return str(self.likeType)


class Reply(models.Model):
    data = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.data


class Comment(models.Model):
    data = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now=True)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE,null=True)
    reply = models.ManyToManyField(Reply, related_name='Reply',null=True)

    def __str__(self):
        return self.data


class Post(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField(Comment,null=True)
    likes = models.ForeignKey(Like, on_delete=models.CASCADE,null=True)
    automate = models.OneToOneField(PostAutomation, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description[:10] + '...'


class Friend(models.Model):
    friends = models.ManyToManyField(User, related_name='Friends')
    bestFriend = models.BooleanField(default=False,null=True)
    created_at = models.DateTimeField(auto_now=True)
    bestFriendCount = models.IntegerField(null=True,)

    def __str__(self):
        return str(self.friends.name)


class Follower(models.Model):
    followers = models.ManyToManyField(User, related_name='Followers')
    followerCount = models.IntegerField(null=True)

    def __str__(self):
        return str(self.followers.name)


class Following(models.Model):
    user_following = models.ManyToManyField(User, related_name='Following')
    followingCount = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user_following.name)


class SocialNodeState(models.Model):
    following = models.OneToOneField(Following,on_delete=models.CASCADE,null=True)
    follower = models.OneToOneField(Follower, on_delete=models.CASCADE,null=True)
    friend = models.OneToOneField(Friend, on_delete=models.CASCADE,null=True)
    posts = models.ManyToManyField(Post, related_name='Posts',null=True)

    def __str__(self):
        return str(self.follower.name)
