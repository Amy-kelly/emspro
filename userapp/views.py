from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def index(request):
    return HttpResponse()

def demo(request):
    print("我是分支,这次正常了")
    return HttpResponse("view完成")

class UserView(View):
    pass