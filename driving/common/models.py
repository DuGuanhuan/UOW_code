from django.db import models


# Create your models here.

class Pic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="图片名字", default='', max_length=100)
    eye_status = models.CharField(verbose_name="眼睛状态", default='', max_length=100)
    yawn = models.BooleanField(verbose_name="是否打哈欠", default=False)
    status = models.BooleanField(verbose_name="是否疲劳", default=False)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pic'