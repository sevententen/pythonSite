# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from UserModel.models import User
from pythonSite import connectDB
from django.shortcuts import render


def login(request):
    return render_to_response('login.html')


def validate(request):
    request.encoding = 'utf-8'
    if 'user' in request.GET:
        username = request.GET['user'].encode('utf-8');
        password = request.GET['password'].encode('utf-8')
        user = connectDB.query(username)
        if user:
            if user.password == password:
                return HttpResponse(username + '欢迎登陆')
            else:
                return HttpResponse("密码不正确")

        else:
            return HttpResponse('用户名不存在')
    return HttpResponse('请输入用户名和密码')



def adduser(request):
    request.encoding = 'utf-8'
    if 'user' in request.GET:
        username = request.GET['user'].encode('utf-8');
        password = request.GET['password'].encode('utf-8')
        return connectDB.adduser(username,password)
    else:
        return HttpResponse('请输入用户名和密码')


def register(request):
    return render_to_response('register.html')