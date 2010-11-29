{% extends 'base_page.tpl' %}
{% block page_content %}
{% include 'forms/post.tpl' %}
<ul>
{% for thread in latest_threads %}
	<li><a href="{% url ib.views.thread board_slug=board.slug thread_id=thread.id %}">{{ thread }}</a></li>
{% endfor %}
</ul>
{% endblock %}
