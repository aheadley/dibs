<hr />
{% if thread.id %}
<form action="{% url ib.views.thread board_slug=board.slug thread_id=thread.id %}" method="post">
{% else %}
<form action="{% url ib.views.board board_slug=board.slug %}" method="post">
{% endif %}
{% csrf_token %}
    <table>
    {{ form.as_table }}
    </table>
    <input type='submit' value='Post' />
</form>
<hr />
