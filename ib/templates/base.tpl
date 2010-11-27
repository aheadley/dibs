<html>
<head>
<title>
{% block head_title %}{{ title }}{% endblock %}</title>
{% block head_meta %}
    {% for name,content in meta %}
    <meta name="{{ name }}" content="{{ content }}" />
    {% endfor %}
{% endblock head_meta %}
{% block head_media %}{% endblock %}
</head>
<body>
{% block body %}{% endblock %}
</body>
</html>
