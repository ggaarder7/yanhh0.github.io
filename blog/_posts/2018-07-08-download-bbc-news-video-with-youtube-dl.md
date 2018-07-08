---
title: Download BBC News Video with Youtube-dl 用youtube-dl下载BBC News的视频
---

一开始用you-get，不行。试了一下youtube-dl居然可以！

I tried you-get first but failed. Surprisingly youtube-dl works.

```
$ youtube-dl https://www.bbc.com/news/av/world-middle-east-44738752/the-mayor-who-wants-a-sexy-police-force
[bbc] the-mayor-who-wants-a-sexy-police-force: Downloading webpage
[bbc] p06d3px1: Downloading media selection XML
[bbc] p06d3px1: Downloading m3u8 information
[bbc] p06d3px1: Downloading m3u8 information
[bbc] p06d3px1: Downloading MPD manifest
[bbc] p06d3px1: Downloading m3u8 information
[bbc] p06d3px1: Downloading m3u8 information
[bbc] p06d3px1: Downloading MPD manifest
[bbc] p06d3px1: Downloading m3u8 information
[bbc] p06d3px1: Downloading m3u8 information
[bbc] p06d3px1: Downloading MPD manifest
[bbc] p06d3px1: Downloading m3u8 information
[bbc] p06d3px1: Downloading m3u8 information
[bbc] p06d3px1: Downloading MPD manifest
[download] Downloading playlist: The mayor who wants a 'sexy' police force
[bbc] playlist The mayor who wants a 'sexy' police force: Collected 1 video ids (downloading 1 of them)
[download] Downloading video 1 of 1
[dashsegments] Total fragments: 39
[download] Destination: The town with 'sexy' shorts on police-p06d3px1.fstream-nonuk-iptv_streaming_concrete_combined_sd_mf_limelight_world_dash_https-video=1570000.mp4
[download]  27.4% of ~25.03MiB at 104.20KiB/s ETA 01:58
...
[download] 100% of 26.63MiB in 02:19
[dashsegments] Total fragments: 39
[download] Destination: The town with 'sexy' shorts on police-p06d3px1.fstream-nonuk-iptv_streaming_concrete_combined_sd_mf_limelight_world_dash_https-audio_eng_1=128000.m4a
[download] 100% of 2.20MiB in 01:02
[ffmpeg] Merging formats into "The town with 'sexy' shorts on police-p06d3px1.mp4"
Deleting original file The town with 'sexy' shorts on police-p06d3px1.fstream-nonuk-iptv_streaming_concrete_combined_sd_mf_limelight_world_dash_https-video=1570000.mp4 (pass -k to keep)
Deleting original file The town with 'sexy' shorts on police-p06d3px1.fstream-nonuk-iptv_streaming_concrete_combined_sd_mf_limelight_world_dash_https-audio_eng_1=128000.m4a (pass -k to keep)
[download] Finished downloading playlist: The mayor who wants a 'sexy' police force
```
