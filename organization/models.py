from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    starostat = models.CharField(max_length=100)
    head_of_starostat = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    pass


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Autor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    watched = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    pass




