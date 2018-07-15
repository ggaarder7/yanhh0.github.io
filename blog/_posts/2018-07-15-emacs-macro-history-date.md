---
title: 'Effectiveness of Emacs Macro: Editing History with Dates'
---

In order to preverse the date as well as the command history, I've set
the `HISTTIMEFORMAT`:

```
$ less ~/.bashrc | grep HIS
HISTTIMEFORMAT="%c "
```

So my `history` output looks like:

```
 6498  Sun Jul 15 16:43:35 2018 move 2014-02-19-jekyll-post-link-hack.md 
 6499  Sun Jul 15 16:43:50 2018 move 2014-11-13-jekyll-includes-are-functions.md 
 6500  Sun Jul 15 16:43:57 2018 move 2015-05-21-rnn-effectiveness.md 
 6501  Sun Jul 15 16:44:05 2018 move 2016-10-21-一种巧妙的绕过Android锁屏密码的方法.md 
 6502  Sun Jul 15 16:44:10 2018 move 2017-07-29-SQL注入绕过技巧.md 
```

However, I need the only commands to be inserted into my blog
article. Here comes the macro.

Step 1. Move the cursor to the beginning (`<CUR>  6498`).

Step 2. `C-x (` to start recording.

Step 3. `C-<SPC> C-u 8 M-f C-f <BACKSPACE>` to remove the dates of the
first line.

Step 4. `C-n C-x )` to return to the initial stage and end recording.

Step 5. `C-u 4 C-x e` to perform.

Step 6. Well done!

```
move 2014-02-19-jekyll-post-link-hack.md 
move 2014-11-13-jekyll-includes-are-functions.md 
move 2015-05-21-rnn-effectiveness.md 
move 2016-10-21-一种巧妙的绕过Android锁屏密码的方法.md 
move 2017-07-29-SQL注入绕过技巧.md 
```
