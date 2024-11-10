from django.contrib import admin
from .models import User



admin.site.site_header = '后台管理系统'
admin.site.site_title = '后台管理系统'
admin.site.index_title = '后台管理'


from django.contrib import  admin
from .models import *


# admin.site.register(qiche)
admin.site.register(User)





