from django.contrib import admin
from .models import Post, Product, Comment,UserInfo,Like,Survey,CardNews_model, Community_model,Community_comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(UserInfo)
admin.site.register(Like)
admin.site.register(Survey)
admin.site.register(CardNews_model)
admin.site.register(Community_model)
admin.site.register(Community_comment)