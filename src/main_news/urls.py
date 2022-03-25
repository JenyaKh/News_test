"""main_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api_news.views import PostCreate, PostList

from api_news.views import PostUpdate

from api_news.views import PostDelete

from api_news.views import CommentCreate, CommentList, CommentUpdate, CommentDelete

from api_news.views import PostUpvote

urlpatterns = [
    path("admin/", admin.site.urls),
    path("post/create", PostCreate.as_view()),
    path("post/list", PostList.as_view()),
    path("post/update/<pk>", PostUpdate.as_view()),
    path("post/delete/<pk>", PostDelete.as_view()),
    path("comment/create", CommentCreate.as_view()),
    path("comment/list", CommentList.as_view()),
    path("comment/update/<pk>", CommentUpdate.as_view()),
    path("comment/delete/<pk>", CommentDelete.as_view()),
    path("post/upvote/<pk>", PostUpvote.as_view()),
]
