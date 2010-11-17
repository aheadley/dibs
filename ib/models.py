from django.db import models

# Create your models here.

class Thread(models.Model):
    #image_src = models.ImageField(max_length=255, upload_to='src/')
    #thumb_src = models.ImageField(max_length=255, upload_to='thumbs/')
    is_spoiler = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    poster_name = models.CharField(max_length=64)
    poster_ip = models.IPAddressField()
    poster_email = models.CharField(max_length=64)
    subject = models.CharField(max_length=128)
    content = models.TextField()
    password = models.CharField(max_length=64)

class Post(Thread):
    thread = models.ForeignKey(Thread, related_name='posts')

class BannedIP(models.Model):
    ip = models.IPAddressField()
