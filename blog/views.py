from django.shortcuts import render,redirect

from .models import Blog, Comment
from django.http import HttpResponse


# Create your views here.

def index(request):
    data = {
        'blogData': Blog.objects.all()
    }
    return render(request, 'index.html', data)


def details(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        parent = request.POST.get('parent')
        if parent:
            obj = Comment.objects.filter(id=parent).first()
            comment = Comment(blog=Blog.objects.get(id=id), name=name, body=body, parent=obj)
            comment.save()
            back = request.META.get('HTTP_REFERER')
            return redirect(back)
        else:
            comment = Comment(blog=Blog.objects.get(id=id), name=name, body=body)
            comment.save()
        back = request.META.get('HTTP_REFERER')
        return redirect(back)
    else:
        data = {
            'blogData': Blog.objects.get(id=id),
            'commentData': Comment.objects.filter(blog=id, parent=None)
        }
        return render(request, 'details.html', data)
