from modulefinder import IMPORT_NAME
from django.shortcuts import render,get_object_or_404

from .models import Post
from .form import CommentForm
# Create your views here.


def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request,'blog/index.html',
     {"posts":latest_post}
     )


def posts(request):
    all_post = Post.objects.all()
    return render(request,'blog/all-post.html',{"all_posts":all_post})

def post_detail(request,slug):
    # identified_post=Post.objects.get(slug=slug)
    identified_post=get_object_or_404(Post,slug=slug)
    comment_form = CommentForm()
    return render(request,'blog/post-detail.html',{
        "postt": identified_post,
        "post_tags" : identified_post.tag.all(),
        "comment_form":comment_form
    })
