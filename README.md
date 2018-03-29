# SubtitlesFixer

Has it ever happened to you when you download a hebrew subtitles files (.srt file for example) and it appears to be Gibbrish?

Well, This script will fix your file so you can watch your movie quietly. You just need to give it input path of the wrongly encoded file, 
and a output path - where to save the fixed file.

If you are not wishing to use the parameters, It will gently ask you for paths using Tkinter, so you could just double-click it. 

The parameters:

```
> converter.py --help
usage: converter.py [-h] [-i INPUT] [-o OUTPUT]

This script fixes wrong encoded subtitles.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file (wrong encoded).
  -o OUTPUT, --output OUTPUT
                        Output file path. The path of the new subtitles file.
```
