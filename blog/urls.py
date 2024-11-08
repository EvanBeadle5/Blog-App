from django.urls import path
from . import views
from .views import (
    ListBlogPost, IndividualPost, 
    CreatePost, DeletePost,
    UpdatePost
    )

'''
    pk - primary key
'''

urlpatterns = [
    path('', ListBlogPost.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', IndividualPost.as_view(), name='individual-post'),
    path('post/new/', CreatePost.as_view(), name='create-post'),
    path('post/<int:pk>/delete/', DeletePost.as_view(), name='delete-post'),
    path('post/<int:pk>/update', UpdatePost.as_view(), name='update-post'),
]