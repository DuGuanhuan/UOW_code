
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('姓名', default='', max_length=50)

    password = models.CharField('密码', default='123', max_length=50)
    image = models.ImageField('图片', upload_to='static/media', default='static/media/default.png')
    phone = models.CharField('邮箱', default='', max_length=50)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    modify_time = models.DateTimeField('最后修改时间', auto_now=True)
    role = models.IntegerField('角色', default=2)
    description = models.TextField('个人描述')

    def __str__(self):
        # return self.name
        return '-'.join([self.name, self.phone])

    class Meta:
        db_table = 'user'
        verbose_name_plural = verbose_name = '用户表'


# class qiche(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField('图片', default='', max_length=200)
#     path = models.CharField('路径', default='', max_length=200)
#     xh = models.CharField('汽车型号', default='', max_length=200)
#     color = models.CharField('汽车颜色', default='', max_length=200)
#     type = models.CharField('汽车类型', default='', max_length=200)
#     xh = models.CharField('汽车型号', default='', max_length=200)
#     create_time = models.DateTimeField('创建时间', auto_now_add=True)
#
#     def __str__(self):
#         # return self.name
#         return '-'.join([self.name, self.xh])
#
#     class Meta:
#         db_table = 'pic'
#         verbose_name_plural = verbose_name = '汽车型号识别表'











