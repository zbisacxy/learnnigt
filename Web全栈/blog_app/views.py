from django.shortcuts import render,redirect
from blog_app.models import BlogPosts,SomeOne,Friend_link,Comment,Image,Bottom,User
from django.contrib.auth.models import AbstractUser
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'GET':
        blog_list = BlogPosts.objects.all()
        some_list  = SomeOne.objects.all()
        friend_link_list = Friend_link.objects.all()
        comment_list = Comment.objects.all()
        bottom_list = Bottom.objects.all()
        return render(request,'index.html',locals())
    else:
        return HttpResponse('POST')


def list(request,category_id,pIndex):
    if category_id == category_id:
        image_list = Image.objects.filter(category_id=category_id)
        p = Paginator(image_list,10)
        if pIndex == None:
            pIndex = 1
        pIndex = int(pIndex)
        image_list = p.page(pIndex)
        list_count = p.page_range
        a=[]
        b=[]
        for num in list_count:
            a.append(num)
            max = a[-1]
            next_down = pIndex+1
            b.append(num)
            min = b[0]
            next_dump = pIndex-1


    return render(request,'list.html',locals())

def Comment_In(request):
    message = ''
    if request.method == 'POST':
        #获取网页上数据
        user = request.POST.get('user')
        comment = request.POST.get('comment')
        if user and comment:
            #判断用户是否存在
            try:
                user = User.objects.get(username = user)
                #实例化评论
                Ins = Comment()
                Ins.user = user
                Ins.comment = comment
                Ins.save()
                return redirect('/index/')
            except:
                message='用户不存在'
                return HttpResponse('用户不存在')

    else:
        return HttpResponse('请求方式有误')

    return render(request,'index.html',locals())

