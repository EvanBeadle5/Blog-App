from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, DetailView, 
    DeleteView, CreateView,
    UpdateView, 
    )

def homePage(request):
    
    #homepage displays all blog posts
    context = {
        'posts': Post.objects.all(),
        'title' : 'Homepage',
    }
    return render(request, 'blog/home.html', context)

class ListBlogPost(ListView):
    '''
        setting template to display blogpost
        naming convention: <app>/<model>_<viewtype>.html
        context_object_name == ListView.object
        ['-date_posted'] orders objects in an ascending view
    '''
    model = Post
    template_name='blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
class ListUserPost(ListView):
    model = Post
    template_name='blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
    #override get_query_set
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class IndividualPost(DetailView):
    model = Post
    
class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    
    #overrides form_valid method
    #sets self.user as the posts author for the post_form before submitting
    #then returns the parent form_valid method with the updated info
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdatePost(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class DeletePost(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})