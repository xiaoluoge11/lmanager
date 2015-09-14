#encoding=utf-8
from django.contrib import admin
from app.models import *


admin.site.register(Idc)
admin.site.register(HostList)
admin.site.register(ServerAsset)
admin.site.register(Group)
admin.site.register(Upload)
admin.site.register(salt_return)
admin.site.register(cmd_run)
