from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # /blog/
    path("posts/", views.posts), # /blog/posts/
    path("posts/my-first-post", views.first_post) # /blog/posts/my-first-post
]