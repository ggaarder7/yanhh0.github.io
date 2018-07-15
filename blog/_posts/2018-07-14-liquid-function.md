---
title: Define Functions in Liquid
---

There are some categories of my posts, and I listed them individually
in the Index, like:

{% raw %}
```
**Starred Posts**

{% for item in site.tags['starred'] %}
  <span>{{ item.date | date: "%b %-d, %Y" }}</span>
  &raquo;
  <a href="{{ item.url | prepend: site.baseurl}}">{{ item.title }}</a>
{% endfor %}

**All Posts**

{% for item in site.posts %}
  <span>{{ item.date | date: "%b %-d, %Y" }}</span>
  &raquo;
  <a href="{{ item.url | prepend: site.baseurl}}">{{ item.title }}</a>
{% endfor %}

**Tabs**

{% for item in site.tabs %}
  <span>{{ item.date | date: "%b %-d, %Y" }}</span>
  &raquo;
  <a href="{{ item.url | prepend: site.baseurl}}">{{ item.title }}</a>
{% endfor %}

**Reprints**

{% for item in site.reprints %}
  <span>{{ item.date | date: "%b %-d, %Y" }}</span>
  &raquo;
  <a href="{{ item.url | prepend: site.baseurl}}">
    {{ item.author }}: {{ item.title }}
  </a>
{% endfor %}
```
{% endraw %}

I don't want to repeat myself. Can them be packaged into a function?
The Liquid documentation doesn't mention about function-like
features. [A Stackoverflow question][so-liquid-function] use `include`
and it works well. Just write:

{% raw %}
```liquid
{% include footer.html param="value" variable-param=page.variable %}
```
{% endraw %}

[so-liquid-function]: https://stackoverflow.com/questions/21976330/passing-parameters-to-inclusion-in-liquid-templates

[A Jekyll user's blog about include][user-blog-include] included more
informations (thanks Jekyll and Markdown, I just grabbed the raw
source from its Github repository to my reprints collection in one
minute).

[user-blog-include]: {% link _reprints_cs/2014-11-13-jekyll-includes-are-functions.md %}
