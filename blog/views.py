from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound
from .models import Post


# Create your views here.

def starting_page(request):

    latest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_posts = sorted(all_posts, key=lambda post: post["date"])
    # latest_posts = sorted_posts[-3:]
 
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):

    all_posts = Post.objects.all().order_by("-date")
    # sorted_posts = sorted(all_posts, key=lambda post: post["date"])

    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):

    identified_post = get_object_or_404(Post, slug=slug)

    # all_posts = Post.objects.all()
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })