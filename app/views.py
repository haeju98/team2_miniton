import json
from django.shortcuts import render, redirect
from .models import Post, Product, Comment, UserInfo, Like, Survey, CardNews
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
# KAKAO API
from project.settings import KAKAO_JS_KEY

# AJAX
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# 1-startpage


def main(request):
    posts = Post.objects.all()
    return render(request, '1-startpage/main.html', {'posts': posts})


# 2-homepage
def home(request):
    posts = Post.objects.all()
    return render(request, '2-homepage/home.html', {'posts': posts})


# 3-Restaurant
def Restaurant(request):
    posts = Post.objects.all().order_by('name')
    sort = request.GET.get('sort', '')  # url의 쿼리스트링을 가져온다. 없는 경우 공백을 리턴한다
    if sort == 'likes':
        posts = Post.objects.filter(likes="True")
        return render(request, '3-Restaurant/Restaurant.html',{'posts':posts})
    elif sort == 'grade':
        posts = Post.objects.all().order_by('-grade')
        return render(request, '3-Restaurant/Restaurant.html',{'posts':posts})
    else:
        return render(request, '3-Restaurant/Restaurant.html',{'posts':posts})

def Restaurant_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    isLike = Like.objects.filter(user_id=User.objects.get(
        pk=request.user.pk), post_id=Post.objects.get(pk=post_pk))


    if(request.method == "POST"):
        Comment.objects.create(
            post=post,
            user_id=request.user,
            content= request.POST['content'],
            grade= float(request.POST['grade'])
        )
        Post.objects.filter(pk=post_pk).update(
            grade=round(Comment.objects.filter(post_id=post_pk).aggregate(Avg('grade'))['grade__avg'],2)
        )
        return redirect('Restaurant_detail', post_pk)
    return render(request, '3-Restaurant/Restaurant_detail.html',{'KAKAO_JS_KEY': KAKAO_JS_KEY, 'isLike': bool(isLike),'post':post, 'post_pk': post_pk})


def post_delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('Restaurant_detail', post_pk)


@csrf_exempt
def like(request):
  
    if request.method == "POST":
        isLike = request.POST.get('isLike') == 'true'
        post_pk = request.POST.get('post_pk')
        if isLike:  # 좋아요 취소
            Like.objects.filter(user_id=User.objects.get(pk=request.user.pk),
                                post_id=Post.objects.get(pk=post_pk)).delete()
            Post.objects.filter(pk=post_pk).update(
            likes = "False"
        )
        else:  # 좋아요 추가
            Like(user_id=User.objects.get(pk=request.user.pk),
                 post_id=Post.objects.get(pk=post_pk)).save()
            Post.objects.filter(pk=post_pk).update(
            likes = "True"
        )
        context = {'message': "성공적으로 완료되었습니다."}
    return HttpResponse(json.dumps(context), content_type="application/json")


def Seongbuk(request):
    # posts=Post.objects.filter(regionname="Seongbuk")
    return render(request, '3-Restaurant/Restaurant_by_Region/Seongbuk.html')#{'posts':posts}


def Mapo(request):
    # posts=Post.objects.filter(regionname="Mapo)
    return render(request, '3-Restaurant/Restaurant_by_Region/Mapo.html')#{'posts':posts}


# 4-Store
def Store(request):
    products = Product.objects.all()
    return render(request, '4-Store/Store.html',{'products':products})

def schoolfood(request):
    products=Product.objects.filter(category="1")
    return render(request, '4-Store/schoolfood.html',{'products':products})#{'posts':posts}

def sidedish(request):
    products=Product.objects.filter(category="2")
    return render(request, '4-Store/sidedish.html',{'products':products})#{'posts':posts}

def sauce(request):
    products=Product.objects.filter(category="3")
    return render(request, '4-Store/sauce.html',{'products':products})#{'posts':posts}

def snack(request): 
    products=Product.objects.filter(category="4")
    return render(request, '4-Store/snack.html',{'products':products})#{'posts':posts}

def meet(request):
    products=Product.objects.filter(category="5")
    return render(request, '4-Store/meet.html',{'products':products})#{'posts':posts}



# 5-Magazine
def Magazine(request):
    posts = Post.objects.all()
    return render(request, '5-Magazine/Magazine.html',{'posts':posts})


# 6-Community
def Community(request):
    posts = Post.objects.all()
    return render(request, '6-Community/Community.html',{'posts':posts})


@login_required(login_url='/registration/login')
def new(request):
    if request.method =='POST':
        new_post =Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.user
        )
        return redirect('Community_detail', new_post.pk)
    return render(request, '6-Community/new.html')

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('Community')

def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method =='POST':
        Post.objects.filter(pk=post_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
        )
        return redirect('Community_detail', post_pk)
    return render(request, '6-Community/edit.html', {'post':post})


def past(request):
    posts = Post.objects.all()
    return render(request, '6-Community/my.html',{'posts':posts})

def Community_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method =="POST":
        Comment.objects.create(
            post=post,
            content=request.POST['content'],
            author=request.user
        )
        return redirect('Community_detail', post_pk)
    return render(request, '6-Community/Community_detail.html',{'post':post})


@login_required(login_url='/registration/login')
def delete_comment(request, post_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('Community_detail', post_pk)

# 7-Recruit
def Recruit(request):
    posts = Post.objects.all()
    return render(request, '7-Recruit/Recruit.html',{'posts':posts})


# registration
def Contactus(request):
    posts = Post.objects.all()
    return render(request, 'registration/Contactus.html',{'posts':posts})


def signup(request):
    if(request.method =="POST"):
        found_user = User.objects.filter(username=request.POST['username'])
        if (len(found_user) >0):
            error = 'username이 이미 존재합니다'
            return render(request, 'registration/signup.html',{'error':error})

        new_user =User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )

        auth.login(
            request,
            new_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return redirect('home')

    return render(request, 'registration/signup.html')


def login(request):
    if (request.method =="POST"):
        found_user =auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if (found_user is None):
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html',{'error':error})

        auth.login(
            request,
            found_user,
            backend='django.contrib.auth.backends.ModelBackend'
        )

        return redirect(request.GET.get('next', '/'))

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
