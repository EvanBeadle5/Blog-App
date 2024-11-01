from django.shortcuts import render
from .models import Post

def homePage(request):
    
    #homepage displays all blog posts
    context = {
        'posts': Post.objects.all(),
        'title' : 'Homepage',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})