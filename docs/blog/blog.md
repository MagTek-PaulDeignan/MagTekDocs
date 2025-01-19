---
title: "Blog"
nav_order: 7
layout: default
parent: blog
permalink: /blog/
---

# Blog

{% for post in site.blog %}
- [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %}
