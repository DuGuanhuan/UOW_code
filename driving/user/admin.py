from django.contrib import admin
from .models import User
admin.site.register(User)


admin.site.site_header = '**后台管理系统'
admin.site.site_title = '**后台管理系统'
admin.site.index_title = '4'