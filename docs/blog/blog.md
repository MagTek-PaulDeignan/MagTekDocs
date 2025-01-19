---
title: Blog
nav_order: 7
layout: home
---

# Blog

{% for post in site.blog %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}
