---
title: Miscellaneous CLI Programs Cheatsheet
---

*Encoding Detect*: enca, chardet (Python module)
*Encoding Convert*: iconv, enconv
*CUE Splitting*: shnsplit (in shntool)

*Split and Compress Music*
```
$ shnsplit -f ../../周杰伦.-.Jay.utf8.cue ../../周杰伦.-.Jay.wav -t "%n %t"
$ for i in *; do ffmpeg -i "$i" -ab 96k "${i/.wav/.aac}"; rm "$i";
done
```

*git*
```
error: file .git/objects/../... is empty
error: file .git/objects/../... is empty
fatal: loose object ... (stored in .git/...) is corrupt
```

- run `git fsck`
- copy the object copy from a backup
- eventually I `git clone`'d a older version, copying all files to
  there then `git commit` all over again

### ffmpeg

[20 FFmpeg Commands For Beginners -
OSTechNix](https://www.ostechnix.com/20-ffmpeg-commands-beginners/)

*Getting audio/video file information*: `ffmpeg -i video.mp4
(-hide_banner)`

*Compress audio*

`ffmpeg -i input.mp3 -ab 128 output.mp3`

The list of various available audio bitrates are:

- 96kbps
- 112kbps
- 128kbps
- 160kbps
- 192kbps
- 256kbps
- 320kbps
