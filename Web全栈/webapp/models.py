from django.db import models

# Create your models here.
class User(models.Model):
    gender = (
        ('mail','男'),
        ('fmail','女')
    )

    name = models.CharField(max_length=30,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=256,verbose_name='密码')
    email = models.EmailField(max_length=128,verbose_name='邮箱',unique=True)
    sex = models.CharField(max_length=5,verbose_name='性别',choices=gender)
    c_time = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
