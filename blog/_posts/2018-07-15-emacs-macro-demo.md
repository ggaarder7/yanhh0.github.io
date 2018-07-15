---
title: A Demo for the Usefulness of Emacs Macro
tags: [ emacs, demo ]
---

I'd like to edit this into one-lines:

```
176 	Montclair State University
Montclair, NJ
176 	Texas Tech University
Lubbock, TX
176 	University of Central Florida
Orlando, FL
176 	University of New Mexico
Albuquerque, NM
183 	Andrews University
Berrien Springs, MI
183 	Azusa Pacific University
Azusa, CA
183 	University of Maine
Orono, ME
183 	West Virginia University
Morgantown, WV
183 	Widener University
Chester, PA
```

Step 1. Move the cursor before `176`.

Step 2. `C-x (` to begin defining macro.

Step 3. `C-n <BACKSPACE> <SPACEx4>` to typesetting the first group
into:

```
176 	Montclair State University    Montclair, NJ
```

Step 4. `C-a C-n` to get back to the initial stage and `C-x )` to end
recording.

Step 5. `C-u 9 C-x e` to apply the macro.

Step 6. `9` is too much. Remove the trailing spaces.

Step 7. Well done!

```
176 	Montclair State University    Montclair, NJ
176 	Texas Tech University    Lubbock, TX
176 	University of Central Florida    Orlando, FL
176 	University of New Mexico    Albuquerque, NM
183 	Andrews University    Berrien Springs, MI
183 	Azusa Pacific University    Azusa, CA
183 	University of Maine    Orono, ME
183 	West Virginia University    Morgantown, WV
183 	Widener University    Chester, PA
```
