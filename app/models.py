from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=50)
    pNumber = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    hours = models.CharField(max_length=50)
    website = models.CharField(max_length=150)
    menu = models.CharField(max_length=50)
    likes = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='writer')
    grade = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.user_id


class UserInfo(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_info')
    user_pw = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    user_number = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)


class Like(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='like_user')
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='like_post')


class Bookmark(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='bookmark_user')
    post_id = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='bookmark_post')


class Survey(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='survey_info')
    problem_1 = models.CharField(max_length=50)
    problem_2 = models.CharField(max_length=50)
    problem_3 = models.CharField(max_length=50)
    problem_4 = models.CharField(max_length=50)
    problem_5 = models.CharField(max_length=50)

#    def result_of_survey(problem_1,problem_2,problem_3,problem_4,problem_5):
#        return result


class CardNews(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
