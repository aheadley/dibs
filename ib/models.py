from django.db import models

# Create your models here.
class Node(models.Model):
    class Meta:
        abstract = True
    #image_src = models.ImageField(max_length=255, upload_to='src/')
    #thumb_src = models.ImageField(max_length=255, upload_to='thumbs/')
    is_spoiler = models.BooleanField(
        default=False)
    timestamp = models.DateTimeField(
        auto_now_add=True)
    poster_name = models.CharField(
        max_length=64,
        blank=True)
    poster_ip = models.IPAddressField(
        default='0.0.0.0')
    poster_email = models.CharField(
        max_length=64,
        blank=True)
    subject = models.CharField(
        max_length=128,
        blank=True)
    content = models.TextField()
    password = models.CharField(
        max_length=64,
        blank=True)

    def __unicode__(self):
        return """Name: %s
        Subject: %s
        Content: %s""" % (self.poster_name, self.subject, self.content)

class Thread(Node):
    last_updated = models.DateTimeField(
        auto_now=True)

    @models.permalink
    def get_absolute_url(self):
        return ('thread_view', (), {'thread_id': self.id})

class Post(Node):
    thread = models.ForeignKey(
        Thread,
        related_name='posts')

class BannedIP(models.Model):
    ip = models.IPAddressField()
