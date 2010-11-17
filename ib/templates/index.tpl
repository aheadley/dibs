<ul>
{% for thread in latest_threads %}
	<li>Thread id: {{ thread.id }}</li>
	<li>Thread posts: <ol>
		{% for post in thread.posts %}
			<li>Post id: {{ post.id }}</li>
		{% endfor %}
	</ol></li>
{% endfor %}
</ul>
