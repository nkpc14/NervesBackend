from django.contrib import admin
from .models import *


admin.site.register(PermissionModel)
admin.site.register(NervesPermission)
admin.site.register(UserCreatedNerve)