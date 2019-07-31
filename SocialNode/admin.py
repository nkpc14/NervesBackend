from django.contrib import admin
from .models import *
admin.site.register(Like)
admin.site.register(Reply)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Friend)
admin.site.register(Follower)
admin.site.register(Following)
admin.site.register(SocialNodeState)
