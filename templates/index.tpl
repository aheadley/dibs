{% extends "base_page.tpl" %}
{% block page_content %}
<ul>
    {% for board in boards %}
    <li><a href="{% url board board_slug=board.slug %}">{{ board.name }}</a></li>
    {% endfor %}
</ul>
{% endblock %}
