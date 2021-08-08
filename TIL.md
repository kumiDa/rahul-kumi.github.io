---
layout: page
title: TIL
description: Today I Learnt
permalink: /til/
categories: learning til
---

{% for entry in site.data.til %}
---
### {{entry["date"]}}
    {% for item in entry.items %}
- #### [{{item.title}}]({{item.url}})
        {% if item.title %}
    {{ item.title }}
        {% endif %}
        {% for tag in item.tags %}
    `{{tag}}`
        {%- endfor %}
    {% endfor %}
{% endfor %}