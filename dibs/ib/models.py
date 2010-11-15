from django.db import models

# Create your models here.

class Thread(models.Model):
    image_src = models.ImageField(max_length=255)
    thumb_src = models.ImageField(max_length=255)
    is_spoiler = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    poster_name = models.CharField()
    poster_ip = IPAddressField()
    poster_email = models.CharField()
    subject = models.CharField()
    content = models.TextField()
    password = models.CharField()

class Post(Thread):
    thread = models.ForeignKey(Thread)
