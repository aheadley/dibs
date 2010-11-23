thread {{ thread.id }}

{% include 'post.tpl' %}

<ul>
{% for post in thread.posts.all %}
    <li> Post: {{ post.id }} </li>
{% endfor %}
</ul>
