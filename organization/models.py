from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    starostat = models.CharField(max_length=100)
    head_of_starostat = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, null=True)
    email = models.EmailField(unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ManyToManyField(User, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    watched = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username
