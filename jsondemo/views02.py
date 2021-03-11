#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author   : linjie
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render #render 把模版和数据一起返回给前台
import json
def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)#这里的地址直接是在templates下面了

def download(request):
    """
    API文档下载
    :param request:
    :return:
    """
    if request.method == "GET":
        file = open('test.txt', 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment;filename="test.txt"'
        return response


'''
3.10 
json数据借口传输实现
linjie
'''
def testjsondata(request):
    data = {
        'patient_name': '张三',
        'age': '25',
        'patient_id': '19000347',
        '诊断': '上呼吸道感染',
    }
    return JsonResponse(data)




'''
3.10
前台分页项目接口
linjie
'''
def getinfo(request):

    # 获取前台分页参数
    page = request.GET.get('page')
    limit = request.GET.get("limit");
    print("分页参数：",page,limit)

    #模拟数据
    datalist = (("111","哈哈哈"),("222","pop"))

    data = []
    for i in datalist:
        # print(i)
        data.append({
            'url': i[0],
            'title': i[1],
        })
    alldata = {"code": 0, "msg": "1", "data": data}
    return JsonResponse(alldata)