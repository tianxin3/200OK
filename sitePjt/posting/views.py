from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post, Comment
from .forms import PostForm, PostNewForm, CommentForm
from .serializers import *
from .models import Post
from friendship import views as FriendshipViews

User = get_user_model()
def ViewPublicPosts(request):
    posts = Post.objects.filter(unlisted=False).order_by('-pub_date')[:50]
    post_list = []
    form = PostNewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            #form.save()
            form_data = form.cleaned_data
            form.cleaned_data['author'] = request.user
            Post.objects.create(**form.cleaned_data)
            form = PostNewForm()
        else:
            print(form.errors)
    
    for post in posts:
        if post.author == request.user:
            post_list.append(post)
        elif post.visibility == 'PUBLIC':
            post_list.append(post)
        elif post.visibility == 'FRIENDS':
            if FriendshipViews.checkFriendship(post.author.id, request.user.id):
                post_list.append(post)
        elif post.visibility == 'FOAF':
            if FriendshipViews.checkFriendship(post.author.id, request.user.id):
                post_list.append(post)
            else:
                for friend in FriendshipViews.getAllFriends(post.author.id):
                    if FriendshipViews.checkFriendship(friend.id, request.user.id):
                        post_list.append(post)
        elif post.visibility == 'SERVERONLY':
            #if author.host == request.user.host:
                #post_list.append(post)
            print("SERVERONLY unimplemented.")
        #if request.user.id in post.visibleTo and (not post in post_list):
            #post_list.append(post)
    context = {
        'post_list': post_list,
        'form': form,

    }

    return render(request, "posting/stream.html", context)

def ViewPostDetails(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "DELETE":
        try:
            post.delete()
        except Exception as e:
            print(e)
        finally:
            return redirect('/service/posts/')

    comments = Comment.objects.filter(post=post)[:10]
    context = {
        'post': post,
        'comment_list': comments,
    }
    return render(request, "posting/post-details.html", context)


def DeletePost(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
    except Exception as e:
        print(e)

    return HttpResponseRedirect(reverse('posting:view user posts', args=(request.user.id,)), {})

def editPost(request, post_id):
    form = request.POST or None
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)
            if form['title']:
                post.title = form['title']
            if form['content']:
                post.content = form['content']
            if form['visibility']:
                post.visibility = form['visibility']
            if form['content_type']:
                post.content_type = form['content_type']
            post.save()
        except Exception as e:
            print(e)
            return render(request, 'post/postDetail.html', {
                'error_message': "Failed to edit post.",
            })

    return HttpResponseRedirect(reverse('posting:view user posts', args=(request.user.id,)), {})

def postCommentHandler(request, post_id, comment_id=None):
    post = Post.objects.get(id=post_id)
    if request.method in ['POST', 'PUT']:
        form = CommentForm(request.POST or None)
        context = {
            "query": "addComment",
            "success": None,
            "message": None,
        }
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['user'] = request.user
            form_data['post'] = post
            comment = Comment(post=post, author=request.user,
                              content=form_data['content'])
            comment.save()
            context['success'] = True
            context['message'] = "Comment Added"
        else:
            print(form.errors)
            context['success'] = False
            context['message'] = "Comment not Allowed"

    return HttpResponseRedirect(reverse('posting:view post details', args=(post_id,)), context)

def deleteComment(request, post_id, comment_id=None):
    post = Post.objects.get(id=post_id)
    context = {
        "query": "deleteComment",
            "success": None,
            "message": None,
    }
    try:
        comment = Comment(id=comment_id)
        comment.delete()
        context['success'] = True
        context['message'] = "Comment deleted"
    except:
        context['success'] = False
        context['message'] = "Delete not Allowed"

    return HttpResponseRedirect(reverse('posting:view post details', args=(post_id,)), context)

def ViewUserPosts(request, author_id):
    author = User.objects.filter(id=author_id)[0]

    if request.method == 'GET':
        posts = Post.objects.filter(author=author)[:10]
        count = len(posts)
        #get from front-end or default
        size = 10
        origin = None
        next = None
        preivous = None

    context = {
        "query": "posts",
        "count": count,
        "size": size,
        "next": next,
        "previous": preivous,
        "posts": posts,
        "allowEdit":True,
    }
    
    return render(request, "posting/user-post-list.html", context)

'''
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        data = Post.objects.all()

        serializer = PostSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PostSerializer(
            post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
