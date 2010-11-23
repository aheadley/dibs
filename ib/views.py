from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from models import Thread, Post
from forms import ThreadForm, PostForm

import datetime

def index(request):
    if request.method == 'POST':
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            thread = thread_form.save(commit=False)
            thread.poster_ip = request.META['REMOTE_ADDR']
            try:
                thread.save()
            except ValueError:
                return HttpResponse('500', status=500)
            else:
                return HttpResponseRedirect(reverse('thread_view', kwargs={'thread_id': thread.id}))

    latest_threads = Thread.objects.all().order_by('-last_updated')[:10]

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
                post = post_form.save(commit=False)
                post.poster_ip = request.META['REMOTE_ADDR']
                post.thread = thread
                try:
                    post.save()
                    if post.poster_email != 'sage':
                        thread.save()
                except ValueError:
                    return HttpResponse('500', status=500)
                else:
                    if post.poster_email == 'noko':
                        return HttpResponseRedirect(reverse('thread_view', kwargs={'thread_id': thread.id}))
                    else:
                        return HttpResponseRedirect(reverse('board_index_view'))

    tpl_vars = {
        'thread': thread,
        'form': PostForm(),
        'action': '/thread/%i/' % thread.id}
    tpl_vars.update(csrf(request))
    return render_to_response('thread.tpl', tpl_vars)