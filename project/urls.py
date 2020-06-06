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
    path('Food/',views.Food,name="Food"),
    path('Cosmetics/',views.Cosmetics,name="Cosmetics"),

    #5-Magazine
    path('Magazine/',views.Magazine,name="Magazine"),

    #6-Community
    path('Community/',views.Community,name="Community"),
    path('Community_detail/<int:post_pk>',views.Community_detail,name="Community_detail"),
    path('delete_comment/<int:post_pk>/<int:comment_pk>',views.delete_comment,name="delete_comment"),
    path('new/',views.new,name="new"),
    path('my/',views.past,name="my"),
    path('delete/<int:post_pk>',views.delete,name="delete"),
    path('edit/<int:post_pk>',views.edit,name="edit"),

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
