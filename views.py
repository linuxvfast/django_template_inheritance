from django.shortcuts import render

# Create your views here.
from app01 import models

def tpl1(request):
    user_list = ['tom','Jias','lin','zeng']
    return render(request,'tpl1.html',{'user_list':user_list})

def tpl2(request):
    user_list = ['db','web','cache']
    return render(request,'tpl2.html',{'user_list':user_list})

def tpl3(request):
    pwd = '123456'
    return render(request,'tpl3.html',{'pwd':pwd})
