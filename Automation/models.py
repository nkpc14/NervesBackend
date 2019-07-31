from django.db import models


class PostAutomation(models.Model):
    post_at = models.DateTimeField()
    status = models.BooleanField(default=False)
