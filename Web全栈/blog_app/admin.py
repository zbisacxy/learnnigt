from django.contrib import admin
from blog_app.models import BlogPosts,User,SomeOne,Friend_link,Comment,Category,Image
# Register your models here.

admin.site.register(BlogPosts)
admin.site.register(User)
admin.site.register(SomeOne)
admin.site.register(Friend_link)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Image)
