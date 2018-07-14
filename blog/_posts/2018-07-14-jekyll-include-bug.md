---
title: Seems Like a Bug in the Include Tag of Liquid in Jekyll
---

I encountered this while editing my index page. I created a template
for generating TOC for a list of posts. However it failed to get the
argument `site.tags['starred']` but successed with all other
`site.posts` `site.reprints` etc. Here's a minimal demo:

```shell
jekyll new demo
cd demo/
echo {% include xxx.html fakearg=site.tags['starred'] %} >> index.md
jekyll serve
```

Then:

```
  Liquid Exception: Invalid syntax for include tag: fakearg=site.tags[starred] Valid syntax: {% include file.ext param='value' param2='value' %} in index.md
jekyll 3.8.3 | Error:  Invalid syntax for include tag:

  fakearg=site.tags[starred]

Valid syntax:

  {% include file.ext param='value' param2='value' %}
```

However, this one will work (just there'll be a error that xxx.html
doesn't exist):

```shell
jekyll new demo
cd demo/
echo {% include xxx.html fakearg=site.posts %} >> index.md
jekyll serve
```
