from django.shortcuts import render
from blog_app.models import BlogContent,Friend_link

# Create your views here.
def index(request):
    if request.method == 'GET':
        blog_list = BlogContent.objects.all()
        friend_link_list = Friend_link.objects.all()
        post_list = BlogContent.objects.order_by('-pub_date').all()[:10]
        return render(request,'index.html',locals())

def single(request,cid):
    friend_link_list = Friend_link.objects.all()
    blog_list = BlogContent.objects.filter(id = cid)
    post_list = BlogContent.objects.order_by('-pub_date').all()[:10]
    return render(request,'single.html',locals())

