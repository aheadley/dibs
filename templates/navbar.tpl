<div class="navbar">
   &lt;|{% for board in navbar_links %} <a href="{% url dibs.views.board board_slug=board.slug %}" name="{{ board.name }}" class="board">{{ board.slug }}</a>|{% endfor %}&gt;
</div>
