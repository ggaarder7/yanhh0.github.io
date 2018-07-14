---
title: Seems Like a Bug in the Include Tag of Liquid in Jekyll
---

Environment:
```
$ jekyll --version
jekyll 3.8.3
$ ruby --version
ruby 2.3.3p222 (2016-11-21) [x86_64-linux-gnu]
$ uname -a
Linux debian 4.9.0-6-amd64 #1 SMP Debian 4.9.88-1+deb9u1 (2018-05-07) x86_64 GNU/Linux
```

I encountered this while editing my index page. I created a template
for generating TOC for a list of posts. However it failed to get the
argument `site.tags['starred']` but successed with all other
`site.posts` `site.reprints` etc. Here's a minimal demo:

{% raw %}
```shell
jekyll new demo
cd demo/
echo {% include xxx.html fakearg=site.tags['starred'] %} >> index.md
jekyll serve
```
{% endraw %}

Then:

{% raw %}
```
  Liquid Exception: Invalid syntax for include tag: fakearg=site.tags[starred] Valid syntax: {% include file.ext param='value' param2='value' %} in index.md
jekyll 3.8.3 | Error:  Invalid syntax for include tag:

  fakearg=site.tags[starred]

Valid syntax:

  {% include file.ext param='value' param2='value' %}
```
{% endraw %}

However, this one will work (just there'll be a error that xxx.html
doesn't exist):

{% raw %}
```shell
jekyll new demo
cd demo/
echo {% include xxx.html fakearg=site.posts %} >> index.md
jekyll serve
```
{% endraw %}
