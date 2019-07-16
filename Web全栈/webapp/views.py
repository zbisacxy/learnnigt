from django.shortcuts import render,redirect
from webapp.models import User


# Create your views here.
def index(request):
    return render(request,'index.html')


def login(request):
    message = ''
    if request.session.get('is_login'):
        return redirect('/index/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        if username and password:
            #去除左右两边空格
            username = username.strip()
            #验证是否在数据库
            try:
                user = User.objects.get(name = username)
            except:
                #数据库里没有这个用户
                message = '用户不存在'
                return render(request,'login.html',locals())

            #验证密码
            if password == user.password:
                #验证成功
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/',locals())
            else:
                message = '密码错误'

    return render(request,'login.html',locals())

def register(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        if username and password and password2 and email:
            # 去除左右两边空格
            username = username.strip()
            # 验证是否在数据库
                # 数据库里没有这个用户
            if password != password2:
                message = '密码不一致'
                return render(request, 'register.html', locals())
            else:
                user = User.objects.filter(name=username)
                if user:
                    message = '用户已存在'
                    return render(request, 'register.html', locals())

                else:
                    username = request.POST.get('username')
                    password = request.POST.get('password1')
                    print('-----------------')
                    print(password)
                    email = request.POST.get('email')
                    ine = User()
                    ine.name = username
                    ine.password = password
                    ine.email = email
                    ine.save()
                    return redirect('/webapp/login/')

        return render(request,'register.html',locals())






    return render(request,'register.html')

def logout(request):
    if not request.session['is_login']:
        return redirect('/index/')
    else:
        request.session.flush()
    return redirect('/index')
