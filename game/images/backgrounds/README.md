# Image asset format and size requirements (1280x720)

Ren'Py does not make any distinction between character and background art, as they're both treated as images. In general, character art needs to be transparent, which means it should be a PNG file. Background art can be JPEG or PNG files.

Let's standardise with 
**PNG** (with transparent backgrounds) for character and foreground objects and 
**JPEG** for **background** images unless there is a compelling argument to do otherwise.

Although Ren'Py can scale the window up and down, we need to decide upon the initial size of the window, the size at which assets should be drawn, and the size at which assets will be at their sharpest.

There are three choices. 1066x600, 1280x720 and 1920x1080. Ren'Py suggests that 1280x720 is a reasonable compromise.

Let's **create assets at 1280x720** pixels unless there is a good or artistic argument to do otherwise.