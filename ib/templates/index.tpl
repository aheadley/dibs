<ul>
    {% for board in boards %}
    <li><a href="{% url ib.views.board board_slug=board.slug %}">{{ board.name }}</a></li>
    {% endfor %}
</ul>
