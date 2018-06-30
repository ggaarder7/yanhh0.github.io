---
title: Blogging on Github.io with Jekyll
tags: [ blog, github.io, jekyll ]
---

# [Jekyll Doc: Writing posts][writing-posts]

[writing-posts]: https://jekyllrb.com/docs/posts/

All posts must have YAML Front Matter.

The post should be named according to the following format:

```
YEAR-MONTH-DAY-title.MARKUP
```

# [Jekyll Doc: YAML Front Matter][front-matter]

[front-matter]: https://jekyllrb.com/docs/frontmatter/

A basic example:

```yaml
---
layout: post
title: Blogging Like a Hacker
---
```

Front Matter Variables are optional: you can just leave it empty! The
set of triple-dashed lines with nothing in between will still get
Jekyll to process your file.

Some variables:

*layout*

If set, this specifies the layout file to use. Use the layout file
name without the file extension. Layout files must be placed in the
_layouts directory.

Using null will produce a file without using a layout file. However
this is overridden if the file is a post/document and has a layout
defined in the frontmatter defaults.

Starting from version 3.5.0, using none in a post/document will
produce a file without using a layout file regardless of frontmatter
defaults. Using none in a page, however, will cause Jekyll to attempt
to use a layout named "none".

*permalink*

If you need your processed blog post URLs to be something other than
the site-wide style (default /year/month/day/title.html), then you can
set this variable and it will be used as the final URL.

*published*

Set to false if you don’t want a specific post to show up when the
site is generated.

To preview unpublished pages, simply run `jekyll serve` or `jekyll
build` with the `--unpublished` switch. Jekyll also has a handy drafts
feature tailored specifically for blog posts.

--------------------------------------------------------------------

Custom Variables

Any variables in the front matter that are not predefined are mixed into the data that is sent to the Liquid templating engine during the conversion. For instance, if you set a title, you can use that in your layout to set the page title:

```html
<!DOCTYPE HTML>
<html>
  <head>
    <title>{{ page.title }}</title>
  </head>
  <body>
    …
```

---------------------------------------------------------------------

Predefined Variables for Posts

*date*

A date here overrides the date from the name of the post. This can be
used to ensure correct sorting of posts. A date is specified in the
format YYYY-MM-DD HH:MM:SS +/-TTTT; hours, minutes, seconds, and
timezone offset are optional.

*category/categories*

Instead of placing posts inside of folders, you can specify one or
more categories that the post belongs to. When the site is generated
the post will act as though it had been set with these categories
normally. Categories (plural key) can be specified as a YAML list or a
space-separated string.

*tags*

Similar to categories, one or multiple tags can be added to a
post. Also like categories, tags can be specified as a YAML list or a
space-separated string.

--------------------------------------------------------------------

Don't repeat yourself

If you don't want to repeat your frequently used front matter
variables over and over, just define defaults for them and only
override them where necessary (or not at all). This works both for
predefined and custom variables.
