---
title: 'Shell Effectiveness: Batch `git mv`'
tags: [ shell, demo ]
---

I'd like to move about one dozen of files from `_reprints/` to
`_reprints_cs/`. In order not to do it one by one:

```shell
$ git mv _reprints/2005-12-15-wikipedia-britannica.md _reprints_cs/
$ commit _reprints/2005-12-15-wikipedia-britannica.md _reprints_cs/2005-12-15-wikipedia-britannica.md
```

I wrote a helper function:

```shell
$ function move {
>   name=`basename $1`
>   git mv "_reprints/$name" "_reprints_cs/$name"
>   commit "_reprints/$name" "_reprints_cs/$name"
> }
```

`commit` is in my `.bashrc`:

```shell
$ set | grep commit -A 3
commit () 
{ 
    git commit "$@" -m'commit'
}
```

We can also use Shell Parameter Expansion `${1#*/}` in place of
`basename $1` here.

Then:

```shell
move _reprints/2006-02-15-gpg-false-positive.md 
move _reprints/2013-04-01-gpg-sign.md 
move _reprints/2013-08-27-mail.md 
```

You may wonder: Why not just send `$name` as parameter instead of
`_reprints/$name`? It is because that `_reprints/$name` is easier to
enter, thanks to auto completion.

After three moves, I found it not convenient enough. New version:

```shell
$ function move {
>   git mv $1 ../_reprints_cs/$1
>   commit $1 ../_reprints_cs/$1
> }
```

Then:

```
move 2014-02-19-jekyll-post-link-hack.md 
move 2014-11-13-jekyll-includes-are-functions.md 
move 2015-05-21-rnn-effectiveness.md 
move 2016-10-21-一种巧妙的绕过Android锁屏密码的方法.md 
move 2017-07-29-SQL注入绕过技巧.md 
```

How convenient!
