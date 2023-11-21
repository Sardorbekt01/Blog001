from django.db import models


# Create your models here.

class MediaUser(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    image = models.ImageField(null=True, default='default.png')

    def __str__(self) -> str:
        return self.last_name   

class Post(models.Model):
    owner = models.ForeignKey(MediaUser, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png')
    text = models.TextField()

