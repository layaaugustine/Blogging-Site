from modulefinder import IMPORT_NAME
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from .models import Post
from .form import CommentForm
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.


def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request,'blog/index.html',
     {"posts":latest_post}
     )


def posts(request):
    all_post = Post.objects.all()
    return render(request,'blog/all-post.html',{"all_posts":all_post})



class SinglePostView(View):

    def get(self,request,slug):

        post= Post.objects.get(slug=slug)
        comment_form = CommentForm()
        context = {
            "postt":post,
            "post_tags":post.tag.all(),
            "comment_form":comment_form,
            "comments":post.comments.all().order_by('-id')   # full comment in perticular post
        }
        return render(request,'blog/post-detail.html',context)

    def post(self,request,slug):
        comment_form = CommentForm(request.POST)
        post= Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)   # because we except 'post' in comment inform.py,we need post of corresponding comment
            comment.post=post
            comment_form.save()
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug]))
        else:
            # post= Post.objects.get(slug=slug)
            context = {
            "postt":post,
            "post_tags":post.tag.all(),
            "comment_form":comment_form,
            "comments":post.comments.all().order_by('-id')
        }
            return render(request,'blog/post-detail.html',context)



class ReadLaterView(View):
    def post(self,request):
        stored_post = request.session.get("stored_post")

        if stored_post is None:
            stored_post=[]
        
        post_id = request.POST["post_id"]

        if post_id not in stored_post:
            stored_post.append(post_id)

        return HttpResponseRedirect("/")
















# def post_detail(request,slug):
#     # identified_post=Post.objects.get(slug=slug)
#     identified_post=get_object_or_404(Post,slug=slug)
#     comment_form = CommentForm()
#     return render(request,'blog/post-detail.html',{
#         "postt": identified_post,
#         "post_tags" : identified_post.tag.all(),
#         "comment_form":comment_form
#     })