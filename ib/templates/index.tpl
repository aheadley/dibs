{% include 'forms/post.tpl' %}
<ul>
{% for thread in latest_threads %}
	<li>Thread id: {{ thread.id }}<br \> {{ thread }} </li>
	    <br \>Posts:
	    <ol>
	    {% for post in thread.posts.all %}
	        <li>{{ post }}</li>
	    {% empty %}
	        <li> No Posts </li>
	    {% endfor %}
	    </ol>
	</li>
{% endfor %}
</ul>
