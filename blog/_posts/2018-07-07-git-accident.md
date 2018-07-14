---
title: A Git Accident
---

My laptop went blackout right after I typed `commit`: I thought I
plugged in the cable but in fact not.

After rebooting, I tried again but git refused to do anything:

```
error: file .git/objects/../... is empty
error: file .git/objects/../... is empty
fatal: loose object ... (stored in .git/...) is corrupt
```

Stackoverflow said the object files are broken, and advised me to copy
the objects from a previous backup. Eventually I `git clone`'d a older
version, copying all files to there then `git commit` all over again.
