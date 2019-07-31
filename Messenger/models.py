from django.db import models


class QuickReplyTemplate(models.Model):
    data = models.CharField(max_length=500)


class QuickReply(models.Model):
    data = models.CharField(max_length=1000)
    templates = models.ManyToManyField(QuickReplyTemplate, related_name='Templates')


class Message(models.Model):
    data = models.CharField(max_length=5000)
    image = models.ImageField(null=True)
    video = models.FileField(null=True, verbose_name='video')

    def __str__(self):
        return self.data


class AutomatedMessage(models.Model):
    status = models.BooleanField(default=False)
    quickReply = models.ForeignKey(QuickReply, on_delete=models.CASCADE)
