---
title: Better post links with Jekyll
author: liabru
source: http://brm.io/jekyll-post-links/
tags: [ jekyll, ruby, hack ]
---

I really quite like jekyll, the static site generator. But one thing I
had an issue with was creating single links to my own posts.

You're probably thinking, duh that's easy, stupid.  It's also easy to
break your own links during development without realising, e.g. if you
change post slugs or titles or your permalink format during a
migration.

Turns out there's already a liquid tag in jekyll called `post_url`,
but that only brings back a URL.  Better, but as I'm lazy, I want the
title too. So I modified the original [post_url source][post_url-src] to
spit out a complete anchor tag with the url and title all pulled from
the post. You can optionally change the link text too.

[post_url-src]: https://github.com/jekyll/jekyll/blob/master/lib/jekyll/tags/post_url.rb

I prefer this to manually typing post links since this helps keep them
up to date during development, even if you change permalinks, and the
compiler will warn if you accidentally a broken link.

Copy the code from below and drop the file in your _plugins directory
and you're good to go.  Or you can get it from github.

Usage of post_link is as follows:

```liquid
{% post_link post text %}
```

Where post is a post in the usual date-slug format.

If text is specified, it uses that as the anchor text, otherwise it's
the post title.

```liquid
module Jekyll
  module Tags
    class PostLinkComparer
      MATCHER = /^(.+\/)*(\d+-\d+-\d+)-([^\s]*)(\s.*)?$/

      attr_accessor :date, :slug, :text

      def initialize(name)
        all, path, date, slug, text = *name.sub(/^\//, "").match(MATCHER)
        raise ArgumentError.new("'#{name}' does not contain valid date and/or title") unless all
        @slug = path ? path + slug : slug
        @date = Time.parse(date)
        @text = text
      end

      def ==(other)
        slug == post_slug(other)
         
        # disabled the date check below (used in post_url.rb)
        # otherwise posts with a custom date front-matter will fail if it's different to the slug
        
        #&& date.year  == other.date.year &&
        #date.month == other.date.month &&
        #date.day   == other.date.day
      end

      private
      def post_slug(other)
        path = other.name.split("/")[0...-1].join("/")
        if path.nil? || path == ""
          other.slug
        else
          path + '/' + other.slug
        end
      end
    end

    class PostLink < Liquid::Tag
      def initialize(tag_name, post, tokens)
        super
        @orig_post = post.strip
        begin
          @post = PostLinkComparer.new(@orig_post)
        rescue
          raise ArgumentError.new <<-eos
Could not parse name of post "#{@orig_post}" in tag 'post_link'.

Make sure the post exists and the name and date is correct.
eos
        end
      end

      def render(context)
        site = context.registers[:site]

        site.posts.each do |p|
          if @post == p
            return "<a href=\"#{ p.url }\">#{ @post.text ? @post.text.strip! : p.title }</a>"
          end
        end

        raise ArgumentError.new <<-eos
Could not find post "#{@orig_post}" in tag 'post_link'.

Make sure the post exists and the name and date is correct.
eos
      end
    end
  end
end

Liquid::Template.register_tag('post_link', Jekyll::Tags::PostLink)
```
