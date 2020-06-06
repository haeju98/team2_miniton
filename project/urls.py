"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #1-startpage
    path('',views.main,name="main"),

    #2-homepage
    path('home/',views.home,name="home"),

    #3-Restaurant
    path('Restaurant/',views.Restaurant,name="Restaurant"),
    path('Restaurant_detail/<int:post_pk>',views.Restaurant_detail,name="Restaurant_detail"),
    path('Restaurant_detail/user/like', views.like, name="like"),
    path('post_delete_comment/<int:post_pk>/<int:comment_pk>', views.post_delete_comment,name="post_delete_comment"),
    path('Seongbuk/',views.Seongbuk,name="Seongbuk"),
    path('Mapo/',views.Mapo,name="Mapo"),

    #4-Store
    path('Store/',views.Store,name="Store"),
    path('Store_detail/<int:product_pk>',views.Store_detail,name="Store_detail"),
    path('schoolfood/',views.schoolfood,name="schoolfood"),
    path('sidedish/',views.sidedish,name="sidedish"),
    path('sauce/',views.sauce,name="sauce"),
    path('snack/',views.snack,name="snack"),
    path('meet/',views.meet,name="meet"),

    #5-Magazine
    path('Magazine/',views.Magazine,name="Magazine"),
    path('Magazine_detail/news1',views.news1,name="news1"),
    path('Magazine_detail/news2',views.news2,name="news2"),
    path('Magazine_detail/news3',views.news3,name="news3"),
    path('Magazine_detail/news4',views.news4,name="news4"),
    path('Magazine_detail/news5',views.news5,name="news5"),
    path('Magazine_detail/news6',views.news6,name="news6"),
    path('Magazine_detail/news7',views.news7,name="news7"),
    path('Magazine_detail/news8',views.news8,name="news8"),

    #6-Community
    path('Community/',views.Community,name="Community"),
    path('Community_detail/<int:post_pk>',views.Community_detail,name="Community_detail"),
    path('delete_comment/<int:post_pk>/<int:comment_pk>',views.delete_comment,name="delete_comment"),
    path('Community_new/',views.Community_new,name="Community_new"),
    path('Community_my/',views.Community_past,name="Community_my"),
    path('Community_delete/<int:post_pk>',views.Community_delete,name="Community_delete"),
    path('Community_edit/<int:post_pk>',views.Community_edit,name="Community_edit"),

    #7-Recruit
    path('Recruit/',views.Recruit,name="Recruit"),

    #registration
    path('registration/signup',views.signup,name="signup"),
    path('registration/login',views.login,name="login"),
    path('registration/logout',views.logout,name="logout"),
    path('Contactus/',views.Contactus,name="Contactus"),
    #social login
    path('accounts/',include('allauth.urls')),
]
