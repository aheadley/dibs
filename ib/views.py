from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Thread, Post
from forms import ThreadForm, PostForm

def index(request):
    latest_posts = Post.objects.all().order_by('-timestamp')[:20]
    latest_threads = []
    for post in latest_posts:
        if post.thread not in latest_threads:
            latest_threads.append(post.thread)
            
    tpl_vars = {
        'latest_threads': latest_threads[:10],
        'form': ThreadForm(),
    }
    tpl_vars.update(csrf(request))

    return render_to_response('index.tpl', tpl_vars)

def thread(request, thread_id):
    try:
        thread = Thread.objects.select_related().get(id=thread_id)
    except Thread.DoesNotExist:
        raise Http404
    else:
        return render_to_response('thread.tpl',
            {'thread': thread,
            'form': PostForm()})

def post(request, thread_id):
    if thread_id is not None:
        try:
            thread = Thread.objects.get(id=thread_id)
        except Thread.DoesNotExist:
            raise Http404
        else:
            post = PostForm(request.POST, request.FILES)
            #this is probably not needed
            post.thread = thread
            try:
                post.save()
            except ValueError:
                raise Http500
            else:
                if post.poster_email is 'noko':
                    return HttpResponseRedirect('/thread/%i/' % (thread.id))
                else:
                    return HttpResponseRedirect('/index')
    else:
        thread = ThreadForm(request.POST, request.FILES)
        if thread.is_valid():
            thread.save()
            return HttpResponseRedirect('index')
        else:
            return render_to_response('post.tpl', {'form': thread})
