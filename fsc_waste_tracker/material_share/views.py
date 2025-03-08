from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post

def index(request):
    latest_posts = Post.objects.order_by('-created_at')[:5]
    context = { "latest_posts": latest_posts }
    return render(request, "material_share/index.html", context)

def new_post(request):
    return HttpResponse("Post a new post here")

def view_post(request, post_id):
    context = { "post": get_object_or_404(Post, pk=post_id) }
    return render(request, "material_share/view_post.html", context)
# Create your views here.
