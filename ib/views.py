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
			{'thread': thread,
			'posts': thread.posts})
