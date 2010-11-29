{% extends 'base_page.tpl' %}
{% block page_content %}
{% include 'forms/post.tpl' %}
<ul>
    <li> {{ thread }} </li>
{% for post in thread.posts.all %}
    <li> {% include 'post.tpl' %} </li>
{% empty %}
    <li> No posts </li>
{% endfor %}
</ul>
{% endblock %}
