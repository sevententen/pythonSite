# -*- coding: utf-8 -*-

from django.http import HttpResponse

from UserModel.models import User

# 数据库操作
def adduser(username,password):
    test1 = User(userName=username,password=password)
    test1.save()
    return HttpResponse("<p>" + 'add user success' + "</p>")


def showAll(request):
    # 初始化
    response = ""
    response1 = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = User.objects.all()
    # 输出所有数据
    for var in list:
        response1 += var.userName + " " + var.password
    response = response1
    return HttpResponse("<p>" + response + "</p>")

def query(usernameParam):
    return User.objects.get(userName=usernameParam)

def delete(request):
    User.objects.all().delete()
    return HttpResponse('delete success');
