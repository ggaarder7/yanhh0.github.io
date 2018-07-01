---
title: My Shell Cheatsheet
---

- `bg` fg but in background

*[grep a file, but show several surrounding
lines](https://stackoverflow.com/questions/9081/grep-a-file-but-show-several-surrounding-lines)*
See `grep -A` `grep -B` and `grep -C` (for after-context,
before-context and context)

## Shell Parameter Expansion

- `${parameter/pattern/string}` replace pattern with string. If pattern
begins with '/', all matches are replaced, or only the first.

See also [bashref][bashref].

[bashref]: http://www.gnu.org/software/bash/manual/bashref.html

- `mount -o ro`
- `openvt` to run a program on a new virtual console

*tablet calculator* Use script languages like Python and Ruby, or bc:
```
$ echo 707425047/1024/1024 | bc
674
```
