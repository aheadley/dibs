{% extends "base.tpl" %}
{% block body %}
{% include "navbar.tpl" %}
<div class="content_wrapper">{% block page_content %}{% endblock %}</div>
{% endblock %}
