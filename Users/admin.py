from django.contrib import admin
from .models import UserAuthentication,UserProfile


admin.site.register(UserAuthentication)
admin.site.register(UserProfile)