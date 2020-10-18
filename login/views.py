from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
"""编写视图框架"""
# Create your views here.
def index(request):
    '''
    首页
    '''
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')

def login(request):

    '''
    登录
    0、不允许重复登录 session
    1、判别请求方法post
    2、拿前台发送过来的数据
    3、判别是否为正常数据
    4、是：则重定向首页
    5、否：还是返回登录页
    '''
    if request.session.get('is_login',None):#不允许重复登录
        return redirect('/index/')

    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        print(f'看看名字和密码：{username}、{pwd}')
        msg = '请检查填写内容'
        if username.strip() and pwd:        #username and pwd都不能为空
            try:
                user = models.User.objects.get(name=username)
            except:
                msg = '用户不存在'
                return render(request, 'login/login.html',{'msg':msg})
            if user.password == pwd:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                print(f'用户名和密码：{username}、{pwd}')
                return redirect('/index/')
            else:
                msg = '密码错误'
                return render(request,'login/login.html',{'msg':msg})
        else:
            return render(request,'login/login.html',{'msg':msg})
    return render(request,'login/login.html')



def logout(request):
    '''
    登出
    '''
    if not request.session.get('is_login',None):
        return redirect('/login/')
    request.session.flush() #清空session所有内容，如果不想的话，就一个个删除del request.session['is_login']
    return redirect('/login/')

