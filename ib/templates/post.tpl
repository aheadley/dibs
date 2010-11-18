{% if form.thread.id %}
<form action='/post/{{form.thread.id}}/' method='post'>
{% else %}
<form action='/post/' method='post'>
{% endif %}
    <table>
    {{ form.as_table }}
    </table>
    <input type='submit' value='Post' />
</form>
