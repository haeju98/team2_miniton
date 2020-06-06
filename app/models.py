from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    pNumber = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    website = models.CharField(max_length=150)
    category =  models.CharField(max_length=50)
    likes = models.CharField(max_length=50)
    grade = models.FloatField(default = 0)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)

    category =  models.CharField(max_length=50)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='writer')
    grade = models.FloatField()
    content = models.TextField()



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

class Survey(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='survey_info')
    problem_1 = models.CharField(max_length=50)
    problem_2 = models.CharField(max_length=50)
    problem_3 = models.CharField(max_length=50)
    problem_4 = models.CharField(max_length=50)
    problem_5 = models.CharField(max_length=50)

    def __str__(self):
        return self.user_id
#    def result_of_survey(problem_1,problem_2,problem_3,problem_4,problem_5):
#        return result


#5-Magazine
class CardNews_model(models.Model):
    title = models.CharField(max_length=50)
    photo = models.ImageField(blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Cardnews_model")

    def __str__(self):
        return self.title

#6-Community
class Community_model(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Community_model")

    def __str__(self):
        return self.title

class Community_comment(models.Model):
    post=models.ForeignKey(Community_model,on_delete=models.CASCADE, related_name='Community_comment')
    content=models.TextField(null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Community_comment")
