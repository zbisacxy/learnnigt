from django.contrib import admin
from blog_app.models import *
# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']

    admin.site.register(BlogContent)
    admin.site.register(Friend_link)