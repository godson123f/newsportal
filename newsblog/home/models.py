from django.db import models


# Create your models here.
class portal(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picture')
    cate = models.CharField(max_length=50)
    desc = models.TextField()


class st(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='picture')
    cate = models.CharField(max_length=50)
    desc = models.TextField()


class slider(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='image')
    cate = models.CharField(max_length=50)
    date = models.DateField()
