---
layout: default
title: Index
---

小鹤双拼是我最近学过最有用的东西之一了！！！打字的时候拿着对照表忘了就
查一周就学会了！！投入产出比极大！！！

**Posts**

{% for item in site.posts %}
  <span>{{ item.date | date: "%b %-d, %Y" }}</span>
  &raquo;
  <a href="{{ item.url | prepend: site.baseurl}}">{{ item.title }}</a>
{% endfor %}

**Edits**

{% for item in site.edits %}
  <span>{{ item.date | date: "%b %-d, %Y" }}</span>
  &raquo;
  <a href="{{ item.url | prepend: site.baseurl}}">{{ item.title }}</a>
{% endfor %}

Thanks [Tom Preston-Werner](http://tom.preston-werner.com/) for styles.

# Wishlist

如果你想送我礼物……

- 电磁炉：替换坏掉的煤气灶
- 加黑瞳孔 让眼睛又黑有有神的美瞳类物（微博“暑假自然变美”） 预算200人民币左右 韩国购
- 不粘饭的电饭煲
- 几米的绘本
  - 向左走向右走

# What's Being Done

- NetEase Cloud Music Tracker
  - Python
  - Android
- Handwritten Signature Generator
- Kindle (mobi) 繁竖明体转换器
- 郭同学的网站

<p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>
