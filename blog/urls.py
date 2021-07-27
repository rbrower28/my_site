from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"), # /blog/
    path("posts/", views.posts, name="posts-page"), # /blog/posts/
    path("posts/<slug:slug>", views.post, name="post-detail-page") # /blog/posts/my-first-post
]