<div class="post {% if post.thread.board.allow_post_spoiler and post.is_spoiler %}spoiler{% endif %}">
    {% if post.subject %}<span class="post_subject">{{ post.subject }}</span>{% endif %}
    <span class="post_name">
    {% if post.poster_email %}
    <a href="mailto:{{ post.poster_email }}" name="{{ post.poster_name }}">{{ post.poster_name }}</a>
    {% else %}
    {{ post.poster_name }}
    {% endif %}
    </span>
    <span class="timestamp">{{ post.timestamp|date:'r' }}</span>
    <span class="post_id">#{{ post.id }}</span>
    <div class="post_content">{{ post.content }}</div>
</div>
