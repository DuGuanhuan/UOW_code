from django.db import models

class Pic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('图片名', default='', max_length=50)

    path = models.CharField('图片路径', default='123', max_length=255)
    xh = models.CharField('型号', default='',max_length=50)
    color = models.CharField('颜色', default='', max_length=50)
    type = models.CharField('车类型', default='小轿车',max_length=50)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pic'


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('车品牌', default='', max_length=50)
    path = models.CharField('车标路径', default='123', max_length=255)
    county = models.CharField('国家', default='',max_length=50)
    desc = models.TextField('介绍')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'car'


class CarKnowledge(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('主题', default='', max_length=50)
    desc = models.TextField('介绍')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'car_knowledge'


class Info(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(default='',max_length=255)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    def __str__(self):
        return self.id

    class Meta:
        db_table = 'info'