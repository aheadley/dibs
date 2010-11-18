from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from models import Thread, Post

def index(request, *pargs):
	latest_posts = Post.objects.all().order_by('-timestamp')[:20]
	latest_threads = []
	for post in latest_posts:
		if post.thread not in latest_threads:
			latest_threads.append(post.thread)

	return render_to_response('index.tpl',
		{'latest_threads': latest_threads[:10]})

def thread(request, thread_id):
	try:
		thread = Thread.objects.select_related().get(id=thread_id)
	except Thread.DoesNotExist:
		raise Http404
	else:
		return render_to_response('thread.tpl',
			{'thread': thread})

def post(request, thread_id):
    if thread_id is not None:
        try:
            thread = Thread.objects.get(id=thread_id)
        except Thread.DoesNotExist:
            raise Http404
        else:
            post = Post(request.POST, request.FILES)
            #this is probably not needed
            post.thread = thread
            try:
                post.save()
            except ValueError:
                raise Http500
            else:
                if post.poster_email is 'noko':
                    return HttpResponseRedirect()
                else:
                    return HttpResponseRedirect()
    
