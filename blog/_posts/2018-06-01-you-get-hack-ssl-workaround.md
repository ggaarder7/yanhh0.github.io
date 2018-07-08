---
title: You-get Hack Bypass the SSL Certificate Verification
tags: [ starred, hack, you-get, python, nix, ssl ]
---

I am using an outdated operation system with whose SSL broken. So
every time I use wget I had to specify the `--no-check-certificate`
option.

[You-get](https://github.com/soimort/you-get) is a downloader good at
scraping videos. However seems it doesn't have similiar options and I
can't use it on that operation system - it keeps saying 'SSL:
CERTIFICATE_VERIFY_FAILED'.

To workaround this, I entered the pdb, finding the function
communicating with urllib and ssl and modified it to force ssl not to
verify.

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
