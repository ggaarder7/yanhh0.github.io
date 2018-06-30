---
title: My Emacs Cheatsheet
---

# Emacs

- `C-x C-s` to save
- `C-x C-c` to exit
- `C-x 1` to keep only one window
- `C-g` to quit a partially entered command
- `C-u N something` repeat
- `C-/ or C-x u` to undo

## move
- `M-v and C-v` to move to the previous or next screen
- `C-p and C-n` to move to the previous or next line
- `C-b and C-f` to move to the previous or next character
- `M-b and M-f` to move to the previous or next word
- `C-a and C-e` to move to the beginning or end of a line
- `M-a and M-e` to move to the beginning or end of a sentence
- `M-< and M->` to move to the beginning or end of the whole text

## delete
- `C-d` to delete the next character
- `M-<DEL> or M-d` to delete the previous or next word
- `C-k` is `d$`
- `C-<SPC>` to begin the mark set
- `C-w` to kill
- `C-y` to yank

## multi-file
- `C-x C-f` to find a file
- `C-x C-b` to list buffers
- `C-x b something` to switch buffer

## Internet

- `M-x package-`

## Modes

- `M-x hexl-mode`
- artist mode
  - C-c C-c: artist mode off

## Macro

- `C-x (` start recording
- `C-x )` stop recording
- `C-x e` play the last record. I often use it with `C-u`.
- `C-x C-k n` name the macro
- `M-x name-of-macro` play back

## Typesetting

- `M-x fill-paragraph` or `M-q` to break a long paragraph into multiple lines.
- `M-x fill-region` to break lines in a text selection.
- `M-x set-fill-column` or `C-x f` to set the max characters per line
  used by 'fill' commands.
- `M-x ruler-mode`
- `M-x auto-fill-mode`
