from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    context = {'title': '测试模板处理数据'}
    return render(request, 'Book/index.html', context)
