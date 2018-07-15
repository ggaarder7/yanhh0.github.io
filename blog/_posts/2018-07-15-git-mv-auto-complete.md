---
title: '`git mv` with Convenient Tab Auto-Complete'
---

Step 1:
1. `git mv a/2018-01-01-<TAB>`
2. -> `git mv a/2018-01-01-blahblahblah.ext`
3. `git mv a/2018-01-01-blahblahblah.ext b/`

Step 2:
1. `<UP>`
2. -> `git mv a/2018-01-01-blahblahblah.ext b/`
3. `commit mv a/2018-01-01-blahblahblah.ext b/`
4. `commit mv a/2018-01-01-blahblahblah.ext b/2018-01-01-<TAB>`
5. `commit mv a/2018-01-01-blahblahblah.ext b/2018-01-01-blahblahblah.ext`

`commit` is in my bashrc:

```shell
commit () 
{ 
    git commit "$@" -m'commit'
}
```
