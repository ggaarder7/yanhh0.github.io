---
title: Blogging on Github.io with Jekyll
tags: [ blog, github.io, jekyll ]
---

*yanhh's note* Learn from others. You can search `.github.io` in
Github. And don't miss [Sites using Jekyll | Jekyll
documentation][sites-using-jekyll] and [a longer list][sites-longer].

[sites-using-jekyll]: https://jekyllrb.com/docs/sites/
[sites-longer]: https://github.com/jekyll/jekyll/wiki/Sites

# [Quick-start][quick-start]

[quick-start]: https://jekyllrb.com/docs/quickstart/

```shell
sudo apt-get install ruby ruby-all-dev ruby-dev build-essential

# Running Jekyll as Non-Superuser (no sudo!)
# You can add these to your bashrc file. Then you can either close and
# restart Bash, logout and log back into your shell account, or run
# `. .bashrc` in the currently-running shell.
export GEM_HOME=$HOME/gems
export PATH=$HOME/gems/bin:$PATH

# Install Jekyll gem through RubyGems
gem install jekyll

# Create a new Jekyll site at ./myblog
jekyll new myblog

# Change into your new directory
cd myblog

# Build the site on the preview server
jekyll serve

# Now browse to http://localhost:4000 as what the output suggests
```

*yanhh's note* the document suggests install Bundler gem too and use
`bundle exec jekyll serve` to build the site on the preview
server. However I went into `Could not locate Gemfile or .bundle/
directory` error with that, while `jekyll serve` just works well. So I
removed commands about Bundler in the above.

To install the Jekyll site into the directory you’re currently in, run
`jekyll new .` If the existing directory isn’t empty, you can pass the
`--force` option with `jekyll new . --force`.

*yanhh's note* I ran `jekyll new . --force` in my `github.io` folder
and used `git diff` to merge the changes.

*yanhh's note* Use `--incremental` to enable incremental build.

*yanhh's note* When things went wrong, we can use `jekyll serve
--verbose` to see which file caused the errors, like:

{% raw %}
```
$ jekyll serve --verbose
  Logging at level: debug
Configuration file: /home/yanhh/home/mine/projects/2018/yanhh0.github.io/_config.yml
         Requiring: kramdown
            Source: /home/yanhh/home/mine/projects/2018/yanhh0.github.io
       Destination: /home/yanhh/home/mine/projects/2018/yanhh0.github.io/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
         Rendering: about.md
  Pre-Render Hooks: about.md
  Rendering Liquid: about.md
  Rendering Markup: about.md
         Requiring: kramdown
  Rendering Layout: about.md
         Rendering: feed.xml
  Pre-Render Hooks: feed.xml
  Rendering Liquid: feed.xml
  Rendering Markup: feed.xml
  Rendering Layout: feed.xml
         Rendering: index.md
  Pre-Render Hooks: index.md
  Rendering Liquid: index.md
  Rendering Markup: index.md
  Rendering Layout: index.md
      Invalid Date: '' is not a valid datetime.
  Liquid Exception: exit in _layouts/post.html
```

*yanhh's note* When `jekyll 3.1.6 | Error:  Address already in use -
bind(2) for 127.0.0.1:4000`, we can `ps aux | grep jekyll` then kill
the old process.

To update: ```gem update jekyll```

*yanhh's note* To update all gems: `gem update`

To upgrade to latest Rubygems, run: ```gem update --system```

# Themes

*yanhh's note* To install theme (for example): `gem install
jekyll-theme-minimal`

# Writing posts

References:
1. [Writing Posts - Jekyll documentation](https://jekyllrb.com/docs/posts/)
2. `welcome-to-jekyll.markdown` created by `jekyll new`

All posts must have YAML Front Matter.

The post should be named according to the following format:

```
YEAR-MONTH-DAY-title.MARKUP
```

*Including images and resources*

Chances are, at some point, you’ll want to include images, downloads,
or other digital assets along with your text content. While the syntax
for linking to these resources differs between Markdown and Textile,
the problem of working out where to store these files in your site is
something everyone will face.

There are a number of ways to include digital assets in Jekyll. One
common solution is to create a folder in the root of the project
directory called something like assets, into which any images, files
or other resources are placed. Then, from within any post, they can be
linked to using the site’s root as the path for the asset to
include. Again, this will depend on the way your site’s (sub)domain
and path are configured, but here are some examples in Markdown of how
you could do this using the absolute_url filter in a post.

Including an image asset in a post:

```markdown
... which is shown in the screenshot below:
![My helpful screenshot]({{ "/assets/screenshot.jpg" | absolute_url }})
```

Linking to a PDF for readers to download:

```markdown
... you can [get the PDF]({{ "/assets/mydoc.pdf" | absolute_url }})
directly.
```

*A typical post* ([1], code snippets at [2])

```markdown
---
layout: post
title:  "Welcome to Jekyll!"
date:   2015-11-17 16:16:01 -0600
categories: jekyll update
---

You’ll find this post in your `_posts` directory. Go ahead and edit it
and re-build the site to see your changes. You can rebuild the site in
many different ways, but the most common way is to run `bundle exec
jekyll serve`, which launches a web server and auto-regenerates your
site when a file is updated.

To add new posts, simply add a file in the `_posts` directory that
follows the convention `YYYY-MM-DD-name-of-post.ext` and includes the
necessary front matter. Take a look at the source for this post to get
an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}
```
{% endraw %}

*yanhh's note* According the following (YAML Front Matter), we don't
have to specify the date manually since it can be guessed from the
filename. However the `index.md` file has no date in its filename, so
if its layout will fail to get `post.date`.

*yanhh's note* To avoid repeating `layout: xxx` in every posts, set
the Front Matter defaults in the `_config.yml` ([Configuration |
Jekyll documentation][config]):

[config]: https://jekyllrb.com/docs/configuration/

```
defaults:
  -
    scope:
      path: ""
      type: "pages"
    values:
      layout: "my-site"
  -
    scope:
      path: "projects"
      type: "pages" # previously `page` in Jekyll 2.2.
    values:
      layout: "project" # overrides previous default layout
      author: "Mr. Hyde"
  -
    scope:
      path: "section/*/special-page.html"
    values:
      layout: "specific-layout"
```

{% assign openTag = '{%' %}

*yanhh's note* To write literal Liquid snippets, use `{{ openTag }}
raw %}` and `{{ openTag }} endraw %}`

[Raw - Liquid template language](https://shopify.github.io/liquid/tags/raw/)

Write literal `{{ openTag }} raw %}` and `{{ openTag }} endraw %}`
with this snippet:

{% raw %}
```
{% assign openTag = '{%' %}
{{ openTag }} raw %}
{{ openTag }} endraw %}
```
{% endraw %}

[liquid - Show raw tags in post generated by jekyll - Stack
Overflow](https://stackoverflow.com/questions/19352368/show-raw-tags-in-post-generated-by-jekyll)
answered Jul 2 '16 at 19:30 by [LeonF](https://stackoverflow.com/users/3554038/leonf)

*Displaying an index of posts*

It’s all well and good to have posts in a folder, but a blog is no use
unless you have a list of posts somewhere. Creating an index of posts
on another page (or in a template) is easy, thanks to the Liquid
template language and its tags. Here’s a basic example of how to
create a list of links to your blog posts:

{% raw %}
```html
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
```
{% endraw %}

*Displaying post categories or tags*

Hey, that’s pretty neat, but what about showing just some of your
posts that are related to each other? For that you can use any of the
variables definable in Front Matter. In the “typical post” section you
can see how to define categories. Simply add the categories to your
Front Matter as a yaml list.

Now that your posts have a category or multiple categories, you can
make a page or a template displaying just the posts in those
categories you specify. Here’s a basic example of how to create a list
of posts from a specific category.

First, in the `_layouts` directory create a new file called
`category.html` - in that file put (at least) the following:

{% raw %}
```html
---
layout: page
---

{% for post in site.categories[page.category] %}
    <a href="{{ post.url | absolute_url }}">
      {{ post.title }}
    </a>
{% endfor %}
```
{% endraw %}

Next, in the root directory of your Jekyll install, create a new
directory called category and then create a file for each category you
want to list. For example, if you have a category blog then create a
file in the new directory called `blog.html` with at least

```html
---
layout: category
title: Blog
category: blog
---
```

In this case, the listing pages will be accessible at
`{baseurl}/category/blog.html`

Although categories and tags are very similar, they are used to group
posts, there are a few differences between them. Categories and
sub-categories create hierarchies that, by default, are reflected in
the directory structure of your site. A post with the following header

```html
---
layout: post
title: A Trip
category: [ blog, travel ]
---
```

will be accessible at
`{baseurl}/blog/travel/year/month/day/A-Trip.html`. On the other hand,
a tagged post

```html
---
layout: post
title: A Trip
tags: [ blog, travel ]
---
```

will be saved as `{baseurl}/year/month/day/A-Trip.html`. It is up to
you to create `{baseurl}/tag/blog.html` and
`{baseurl}/tag/travel.html` the same way as described above for
categories.

# [Linking to pages](https://jekyllrb.com/docs/templates/#link)

Like:

{% raw %}
```
{{ site.baseurl }}{% post_url 2010-07-21-name-of-post %}
{{ site.baseurl }}{% post_url /subdir/2010-07-21-name-of-post %}

{{ site.baseurl }}{% link _collection/name-of-document.md %}
{{ site.baseurl }}{% link _posts/2016-07-26-name-of-post.md %}
{{ site.baseurl }}{% link news/index.html %}
{{ site.baseurl }}{% link /assets/files/doc.pdf %}

[Link to a document]({{ site.baseurl }}{% link _collection/name-of-document.md %})
[Link to a post]({{ site.baseurl }}{% link _posts/2016-07-26-name-of-post.md %})
[Link to a page]({{ site.baseurl }}{% link news/index.html %})
[Link to a file]({{ site.baseurl }}{% link /assets/files/doc.pdf %})
```
{% endraw %}

# [YAML Front Matter][front-matter]

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



# [Collections][collections]

[collections]: https://jekyllrb.com/docs/collections/

Not everything is a post or a page. Maybe you want to document the
various methods in your open source project, members of a team, or
talks at a conference. Collections allow you to define a new type of
document that behave like Pages or Posts do normally, but also have
their own unique properties and namespace.

*Step 1: Tell Jekyll to read in your collection*

Add the following to your site’s `_config.yml` file, replacing
my_collection with the name of your collection:

```
collections:
- my_collection
```

You can optionally specify metadata for your collection in the
configuration:

```
collections:
  my_collection:
    foo: bar
```

Default attributes can also be set for a collection:

```
defaults:
  - scope:
      path: ""
      type: my_collection
    values:
      layout: page
```

You can optionally specify a directory to store all your collections
in the same place with `collections_dir: my_collections`.

Then Jekyll will look in `my_collections/_books` for the books
collection, and in `my_collections/_recipes` for the recipes
collection.

If you specify a directory to store all your collections in the same
place with `collections_dir: my_collections`, then you will need to
move your `_drafts` and `_posts` directory to `my_collections/_drafts`
and `my_collections/_posts`. Note that, the name of your collections
directory cannot start with an underscore (`_`).

*Step 2: Add your content*

Create a corresponding folder (e.g. *<source>/_my_collection*) and add
documents. YAML front matter is processed if the front matter exists,
and everything after the front matter is pushed into the document’s
content attribute. If no YAML front matter is provided, Jekyll will
not generate the file in your collection.

*Step 3: Optionally render your collection’s documents into
independent files*

If you’d like Jekyll to create a public-facing, rendered version of
each document in your collection, set the output key to true in your
collection metadata in your *_config.yml*:

```
collections:
  my_collection:
    output: true
```

This will produce a file for each document in the collection. For
example, if you have `_my_collection/some_subdir/some_doc.md`, it will
be rendered using Liquid and the Markdown converter of your choice and
written out to `<dest>/my_collection/some_subdir/some_doc.html`.

If you wish a specific page to be shown when accessing
`/my_collection/`, simply add permalink: `/my_collection/index.html`
to a page. To list items from the collection, on that page or any
other, you can use:

{% raw %}
```html
{% for item in site.my_collection %}
  <h2>{{ item.title }}</h2>
  <p>{{ item.description }}</p>
  <p><a href="{{ item.url }}">{{ item.title }}</a></p>
{% endfor %}
```
{% endraw %}
