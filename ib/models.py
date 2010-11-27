from django.db import models

class Board(models.Model):
    max_threads = models.PositiveIntegerField(
        default=100,
        blank=False)
    allow_thread_image = models.BooleanField(
        default=True)
    require_thread_image = models.BooleanField(
        default=True)
    allow_thread_spoiler = models.BooleanField(
        default=False)
    allow_post_image = models.BooleanField(
        default=True)
    require_post_image = models.BooleanField(
        default=False)
    allow_post_spoiler = models.BooleanField(
        default=True)
    disable_sage = models.BooleanField(
        default=False)
    safe_for_work = models.BooleanField(
        default=False)
    slug = models.SlugField(
        max_length=32,
        unique=True,
        blank=False)
    name = models.CharField(
        max_length=128,
        blank=False)
    subtext = models.CharField(
        max_length=128,
        blank=True)

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
    board = models.ForeignKey(
        Board,
        related_name='threads')
    last_updated = models.DateTimeField(
        auto_now=True)

    @models.permalink
    def get_absolute_url(self):
        return ('thread_view', (), {
            'board_slug': self.board.slug,
            'thread_id': self.id})

class Post(Node):
    thread = models.ForeignKey(
        Thread,
        related_name='posts')

class BannedIP(models.Model):
    ip = models.IPAddressField()
