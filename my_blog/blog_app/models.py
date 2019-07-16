from django.db import models
from DjangoUeditor.models import UEditorField

class BlogContent(models.Model):
    title = models.CharField('标题', max_length=50)
    content = UEditorField()
    pub_date = models.DateTimeField('发布日期', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '首页博客'
        verbose_name_plural = verbose_name

class Friend_link(models.Model):
    name = models.CharField('名称',max_length=30)
    link = models.CharField('href',max_length=150)
    def __str__(self):
        return self.name
    class Meta:

        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

