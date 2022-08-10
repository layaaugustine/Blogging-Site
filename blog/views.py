from django.shortcuts import render,get_object_or_404

from .models import Post
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

    return render(request,'blog/post-detail.html',{
        "postt": identified_post,
        "post_tags" : identified_post.tag.all()
    })
