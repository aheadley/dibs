{% include 'forms/post.tpl' %}

<ul>
    <li> {{ thread }} </li>
{% for post in thread.posts.all %}
    <li> {{ post }} </li>
{% empty %}
    <li> No posts </li>
{% endfor %}
</ul>
