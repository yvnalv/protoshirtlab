from django.contrib import admin
from app_proto.models import SLUser,AdminUser

# Register your models here.

admin.site.register(SLUser)
admin.site.register(AdminUser)
