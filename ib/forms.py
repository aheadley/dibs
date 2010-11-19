from models import Thread, Post
from django.forms import ModelForm

class ThreadForm(ModelForm):
    class Meta:
        model = Thread

class PostForm(ModelForm):
    class Meta:
        model = Post
