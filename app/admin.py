from django.contrib import admin
from .models import Post, Comment,UserInfo,Like,Bookmark,Survey,CardNews

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserInfo)
admin.site.register(Like)
admin.site.register(Bookmark)
admin.site.register(Survey)
admin.site.register(CardNews)