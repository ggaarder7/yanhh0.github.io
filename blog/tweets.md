---
title: Tweets
---

{% for item in include.collection %}
  <h2>{{ item.title }}</h2>
  <time datetime='{{ item.date | date_to_xmlschema }}'>
    {{ item.date | date: "%b %-d, %Y" }}
  </time>
  <div class="post-content" itemprop="articleBody">
    {{ item.content }}
  </div>
{% endfor %}
