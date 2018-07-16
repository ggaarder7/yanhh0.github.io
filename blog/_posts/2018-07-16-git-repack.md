---
title: Force Git to Pack
---

`git repack -ad`

```
-a
Instead of incrementally packing the unpacked objects, pack
everything referenced into a single pack. Especially useful when
packing a repository that is used for private development. Use with
-d. This will clean up the objects that git prune leaves behind,
but git fsck --full --dangling shows as dangling.

Note that users fetching over dumb protocols will have to fetch the
whole new pack in order to get any contained object, no matter how
many other objects in that pack they already have locally.

-d
After packing, if the newly created packs make some existing packs
redundant, remove the redundant packs. Also run git prune-packed to
remove redundant loose object files.
```

> Especially useful when packing a repository that is used for private
> development. Use with -d. This will clean up the objects that git
> prune leaves behind.
