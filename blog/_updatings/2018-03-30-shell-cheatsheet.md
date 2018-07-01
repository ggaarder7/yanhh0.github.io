---
title: My Shell Cheatsheet
---

- `openvt` to run a program on a new virtual console
- `bg` fg but in background
- `mount -o ro`

*[grep a file, but show several surrounding
lines](https://stackoverflow.com/questions/9081/grep-a-file-but-show-several-surrounding-lines)*
See `grep -A` `grep -B` and `grep -C` (for after-context,
before-context and context)

## Shell Parameter Expansion

- `${parameter/pattern/string}` replace pattern with string. If pattern
begins with '/', all matches are replaced, or only the first.

See also [bashref][bashref].

[bashref]: http://www.gnu.org/software/bash/manual/bashref.html
