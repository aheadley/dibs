from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from models import Thread, Post
from forms import ThreadForm, PostForm

def index(request):
    if request.method == 'POST':
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            #thread = Thread(thread_form)
            try:
                thread_form.save()
            except ValueError:
                return HttpResponse('500', status=500)
            else:
                return HttpResponseRedirect('/thread/%i' % thread_form.id)

    latest_threads = []
    for post in Post.objects.all().order_by('-timestamp'):
        if post.thread not in latest_threads:
            latest_threads.append(post.thread)
        if len(latest_threads) > 10:
            break

    tpl_vars = {
        'latest_threads': latest_threads,
        'form': ThreadForm(),
        'action': '/ib/index',
    }
    tpl_vars.update(csrf(request))

    return render_to_response('index.tpl', tpl_vars)

def thread(request, thread_id):
    try:
        thread = Thread.objects.select_related().get(id=thread_id)
    except Thread.DoesNotExist:
        raise Http404
    else:
        if request.method == 'POST':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post = Post(post_form.cleaned_data)
                post.thread = thread
                try:
                    post.save()
                except ValueError:
                    return HttpResponse('500', status=500)
                else:
                    return HttpResponseRedirect('/ib/index')

        return render_to_response('thread.tpl',
            {'thread': thread,
            'form': PostForm(),
            'action': '/thread/%i/' % thread.id})