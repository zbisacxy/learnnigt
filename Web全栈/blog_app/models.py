from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=30,verbose_name='用户名',default='')


class Category(models.Model):
    name=models.CharField(verbose_name="分类名称",max_length=20,default='')
    class Meta:
        verbose_name="分类"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class BlogPosts(models.Model):
    user = models.ForeignKey(User, verbose_name='作者')
    title = models.CharField('标题', max_length=50)
    content = models.TextField('内容')
    pub_date = models.DateTimeField('发布日期', auto_now_add=True)
    cover = models.ImageField('封面', default=None)
    category = models.ForeignKey(Category, verbose_name='分类')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '主页内容'
        verbose_name_plural = verbose_name

class SomeOne(models.Model):
    user = models.ForeignKey(User, verbose_name='作者')
    head_image = models.ImageField('头像',default='')
    Zwjs = models.CharField('自我介绍', max_length=150)
    class Meta:
        verbose_name = '个人资料'
        verbose_name_plural = verbose_name

class Friend_link(models.Model):
    name = models.CharField('名称',max_length=30)
    link = models.CharField('href',max_length=150)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    comment = models.CharField('评论',max_length=100)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name



class Image(models.Model):
    category = models.ForeignKey(Category,verbose_name='分类')
    image = models.ImageField(verbose_name="图片")
    class Meta:
        verbose_name="图片"
        verbose_name_plural=verbose_name

class Bottom(models.Model):
    image = models.CharField('图片',max_length=200)
    class Meta:
        verbose_name = '底部图片'
        verbose_name_plural = verbose_name

