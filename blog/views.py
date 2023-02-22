from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    post = request.GET.get('post')
    title = request.GET.get('title')
    if post == "" or Post.objects.filter(post_value = post):
        pass
    else:
        data_post = Post(post_title=title,post_value=post)
        # data_post.save()

    posts = Post.objects.all()
    x ={
        'post':posts
    }
    return render(request, 'index.html',x)


def post(request, pk):
    get_post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post':get_post})