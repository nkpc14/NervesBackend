from django.contrib import admin
from .models import *


admin.site.register(QuickReplyTemplate)
admin.site.register(QuickReply)
admin.site.register(Message)
admin.site.register(AutomatedMessage)
