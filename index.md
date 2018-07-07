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

**Thanks [Tom Preston-Werner](http://tom.preston-werner.com/) for TOC style.**

# Wishlist

如果你想送我礼物……

- 几米的绘本
  - 向左走向右走
- 有点贵不想买暂时又可有可无的乐谱
  - 肖邦圆舞曲集
  - 肖邦练习曲集
  - 巴赫英国组曲
  - 巴赫法国组曲
  - 巴赫歌德堡变奏曲
  - 巴赫平均律
  - 巴赫创意曲
  - 贝多芬钢琴奏鸣曲集
  - 帕格尼尼吉他奏鸣曲

# What's Being Done

- NetEase Cloud Music Tracker
  - Python
  - Android
- Handwritten Signature Generator
- Kindle (mobi) 繁竖明体转换器
- 郭同学的网站

# Links

- [Tom Preston-Werner](http://tom.preston-werner.com/)
- [matrix67的博客](http://www.matrix67.com/),
  [考据癖](http://localhost-8080.com/)
- [许嵩的新浪博客](http://blog.sina.com.cn/vae),
  [许嵩的网易博客（停止更新）](http://vaevip.blog.163.com/)

<p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>
