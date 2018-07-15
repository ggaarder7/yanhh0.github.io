---
title: You-get Hack Bypass the SSL Certificate Verification You-get Hack 绕过SSL验证
tags: [ starred, hack, you-get, python, nix, ssl ]
---

I am using an outdated operation system with whose SSL broken. So
every time I use wget I had to specify the `--no-check-certificate`
option.

我的操作系统比较老，SSL已经失效。每次用wget都要指定`--no-check-certificate`参数。

[You-get](https://github.com/soimort/you-get) is a downloader good at
scraping videos. However seems it doesn't have similiar options and I
can't use it on that operation system - it keeps saying 'SSL:
CERTIFICATE_VERIFY_FAILED'.

[You-get](https://github.com/soimort/you-get) 是一个视频下载器，但是它没有
类似的参数，所以根本用不了：每次都说'SSL: CERTIFICATE_VERIFY_FAILED'

To workaround this, I entered the pdb, finding the function
communicating with urllib and ssl and modified it to force ssl not to
verify.

所以我进pdb，找到you-get里与urllib和ssl沟通的函数，改了一下，强行绕过SSL验证。

Code here:

```diff
diff --git a/src/you_get/common.py b/src/you_get/common.py
index e300085..2f0c895 100755
--- a/src/you_get/common.py
+++ b/src/you_get/common.py
@@ -6,6 +6,7 @@ import re
 import sys
 import time
 import json
+import ssl
 import socket
 import locale
 import logging
@@ -381,7 +382,8 @@ def urlopen_with_retry(*args, **kwargs):
     retry_time = 3
     for i in range(retry_time):
         try:
-            return request.urlopen(*args, **kwargs)
+            context = ssl._create_unverified_context()
+            return request.urlopen(*args, **kwargs, context=context)
         except socket.timeout as e:
             logging.debug('request attempt %s timeout' % str(i + 1))
             if i + 1 == retry_time:
```
