<form action='{{ target }}' method='post'> {% csrf_token %}
    <table>
    {{ form.as_table }}
    </table>
    <input type='submit' value='Post' />
</form>
