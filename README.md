# Source Han SimSun

Make Source Han Serif* as SimSun! If you hate SimSun, This repo can help you.

Type `make` and you'll get `simsun.ttc`, `simsunl.ttc` and `simsunbd.ttc`.

And you should install them on Windows as administrator.

*: Actually, It's [Dream Han Serif](https://github.com/Pal3love/dream-han-cjk), a ttf variant of Source Han Serif.

# Dependence

- afdko
- fontTools

```
pip3 install afdko fonttools
```
- make (optional)

It needs *nix environment. You can run the commands in Makefile if you are using Windows.

# Several Issues

- NSimSun should be monospace font
- ~~The single line spacing in MS Office is bigger than the original SimSun~~ (Fixed with [USE_TYPO_METRICS flag ON in OS/2 Table](https://learn.microsoft.com/en-us/typography/opentype/spec/os2#fsselection), which is flagged ON in SimSun as well.)

# Standard Disclaimer

```c
#include <std_disclaimer.h>

/*
* Please do some research if you have any concerns about features included 
* in this repo before applying it! YOU are choosing to make these modifications, 
* and if you point the finger at us for messing up your device, we will laugh 
* at you.
*/
```