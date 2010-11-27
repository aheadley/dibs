from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from models import *
from forms import ThreadForm, PostForm

import datetime

def index(request):
    boards = Board.objects.all()
    return render_to_response('index.tpl', {'boards': boards})

def board(request, board_slug):
    try:
        board = Board.objects.get(slug__iexact=board_slug)
    except Board.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        thread_form = ThreadForm(request.POST)
        if thread_form.is_valid():
            thread = thread_form.save(commit=False)
            thread.poster_ip = request.META['REMOTE_ADDR']
            thread.board = board
            try:
                thread.save()
            except ValueError:
                return HttpResponse('500', status=500)
            else:
                return HttpResponseRedirect(
                    reverse('thread_view',
                    kwargs={
                        'board_slug': board.slug,
                        'thread_id': thread.id}))

    latest_threads = Thread.objects.filter(board=board).order_by('-last_updated')[:10]

    tpl_vars = {
        'board': board,
        'latest_threads': latest_threads,
        'form': ThreadForm(),
    }
    tpl_vars.update(csrf(request))
    return render_to_response('board.tpl', tpl_vars)

def thread(request, board_slug, thread_id):
    try:
        board = Board.objects.get(slug__iexact=board_slug)
        thread = Thread.objects.select_related().get(id__exact=thread_id)
    except ObjectDoesNotExist:
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
                        return HttpResponseRedirect(
                            reverse('thread_view',
                            kwargs={'board_slug': board.slug,
                                'thread_id': thread.id}))
                    else:
                        return HttpResponseRedirect(
                            reverse('board_view',
                            kwargs={'board_slug': board.slug}))

    tpl_vars = {
        'board': board,
        'thread': thread,
        'form': PostForm()}
    tpl_vars.update(csrf(request))
    return render_to_response('thread.tpl', tpl_vars)