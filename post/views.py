from django.shortcuts import render
from django.http import HttpResponse
from post.models import *
# Create your views here.
def index(request):
    from django.template import Template
    t = Template('{{name}}:你好<br>{%for data in datas%}{{data}}{%endfor%}')
    from django.template.context import Context
    c = Context({'name':'李四','datas':range(10)})
    content = t.render(c)
    return HttpResponse(content)

def post(request):
    return HttpResponse('我是帖子详情')

def getAllCategory(request):
    return render(request,'post/category.html',{'categorys':Category.objects.all()})

def get_post_by_category(request, categoryid):
    cate = Category.objects.get(id = categoryid)
    return render(request,'post/category_details.html',{'posts':cate.post_set.all()})