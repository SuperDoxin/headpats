# headpats
 A simple pygame script for generating HEADPATS animations, [like so](https://twitter.com/Foone/status/1215479542959075328)

 I've included sample images for [a windows 3.1 icon](https://twitter.com/win_icons/status/1215392811354247168) and [my twitter avatar](https://twitter.com/Foone). 

## Requirements:
* [Python 2.7](https://www.python.org/)
* [pygame](https://www.pygame.org/news) (tested with 1.9.5)

## Customizing

headpats.py accepts the following optional arguments:

```
  -h, --help            show this help message and exit
  --background-image BACKGROUND_IMAGE
                        set the path for the background image to use
  --hand-image HAND_IMAGE
                        set the path for the hand image to use
  -f, --fullscreen      start fullscreen
  --pats-per-second PATS_PER_SECOND
                        set pat frequency
  --pat-amplitude PAT_AMPLITUDE
                        set pat amplitude
  -x PAT_X, --pat-x PAT_X
                        set horizontal pat position
  -y PAT_Y, --pat-y PAT_Y
                        set vertical pat position
  --framerate FRAMERATE
                        set the frame rate limit. 0 or lower disables the
                        frame rate limit.
```
## Capturing

I didn't build in any function to directly create the GIFs, I instead captured the program running using [OBS](https://obsproject.com/).

## License

All code is GPL3. The example images come from iconart.dll and Microsoft Windows 95.
