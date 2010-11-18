{% include 'post.html' %}
<ul>
{% for thread in latest_threads %}
	<li>Thread id: {{ thread.id }}</li>
	    Posts:
	    <ol>
	    {% for post in thread.posts.all %}
	        <li>{{ post.id }}</li>
	    {% endfor %}
	    </ol>
	</li>
{% endfor %}
</ul>
