from models import Thread, Post
from django.forms import ModelForm

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        exclude = (
        #set automatically in database
            'timestamp',
        #set manually in view
            'poster_ip',
            'last_updated',
            'board',
        )

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = (
        #set automatically in database
            'timestamp',
        #set manually in view
            'poster_ip',
            'thread',
        )