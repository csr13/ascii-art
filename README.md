## ASCII ART

A set of scripts for asciifying images, can be run locally or via docker container.

### Docker Setup (Recommended)

Build the image
```
~$ docker build --tag=art:latest .
```

To run the container, it is necesary to mount two bind volumes so that the ouput can be inspected on the local machine

Examples.

```
~$ docker run -it -e script_name=image_segmentation \
  --mount type=bind,source=$(pwd)/src/images/,target=/src/images/ \
  --mount type=bind,source=$(pwd)/src/output/,target=/src/output/ \
  --name=art \
  --rm \
  art:latest image_segmentation -h

~$ docker run -it -e script_name=image_segmentation \
  --mount type=bind,source=$(pwd)/src/images/,target=/src/images/ \
  --mount type=bind,source=$(pwd)/src/output/,target=/src/output/ \
  --name=art \
  --rm \
  art:latest swapper -h
```

---

### Local Machine Setup

#### Requirements:

- Python3.8 >
- Debian (Ubuntu 18.04, 20.04) - Tested

Within the `/src` directory of the project, add a directory called `images`, within
this directory include all the images you want to conver to ascii. In addition, create
also within `/src` create another directory called `output` which will be where the rendered art
will be generated.

Install dependencies
```bash
:~$ python3.8 -m pip install -r requirements.txt
```

Depending on installation u might need to install `cv2` required libraries
```
apt-get update -y && \
    apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6
```
---

### Examples

Every script has it's own help menu and you can trigger it by running the script with
the --help flag, below is the output of each of the scripts
Usable Scripts:
- `image_segmentation`
- `swapper`


Options for `image_segmentation` script, this takes image name from any image on `images` folder and applies some asciification depending on given arguments.
```
usage: image_segmentation [-h] [--scale-factor 0.05] [--char-width 9] [--char-height 9] [--color COLOR [COLOR ...]] [--superimpose {yes,no}] image {white,black} 0 0 0 0 [0 0 0 0 ...] 57 png

Does some image segmentation on coordinates, and users swapper functionality and thats it.

positional arguments:
  image                 [INFO] Image location relative.
  {white,black}         [INFO] select choice - white or black.
  0 0 0 0               [INFO] Coordenates to crop, left, upper, right, lower
  57                    [INFO] Threshold for white and black images
  png                   [INFO] Image output format

options:
  -h, --help            show this help message and exit
  --scale-factor 0.05   [INFO] scale factor for swapper
  --char-width 9        [INFO] char width for swapper
  --char-height 9       [INFO] char height for swapper
  --color COLOR [COLOR ...]
                        [INFO] Color for the rendering defaults to 0 0 0
  --superimpose {yes,no}
                        To superimpose the image back onto
```
#### image_segmentation practical example.

Run `image_segmentation` on an image sky.jpeg where the whites of the image will be asciified, only apply to coordenates left, upper, right, lower, apply 133 (agression for asciification) scale factor of the asciification to 0.22 character width 10 character height 10 and apply color red to asciification.
```
~$ docker run -it -e script_name=image_segmentation \
  --mount type=bind,source=$(pwd)/src/images/,target=/src/images/ \
  --mount type=bind,source=$(pwd)/src/output/,target=/src/output/ \
  --name=art \
  --rm \
  art:latest sky.jpeg white 0 0 1000 1000 133 png --scale-factor=0.22 --char-width=10 --char-height=10 --color 255 0 0
```

> It is important to notice that if given wrong coordinates there will be a segmentation fault, but if your give inaccurate coordinates the program will throw an exception with a informative exception message.
---

Options for `swapper` script, scripts takes all images and asciifies them
```
usage: swapper [-h] [-c 69 [69 ...]] [-cw 18] [-ch 9] [-sf 0.18] [-l arabic] [-fs 19] [-sw 2] [-nc yes]

options:
  -h, --help            show this help message and exit
  -c 69 [69 ...], --color 69 [69 ...]
                        [INFO] The color for the picture, represented by RGB specification, eg: --color 255 255 255 -- defaults to 0 0 0 (black)
  -cw 18, --char-width 18
                        [INFO] The width of the characters, eg: --char-width 18 -- defaults to 9
  -ch 9, --char-height 9
                        [INFO] The height of the character, eg: --char-height 9 -- defaults to 9
  -sf 0.18, --scale-factor 0.18
                        [INFO] Scale factor of the image, eg: 0.20 -- defaults to 0.18
  -l arabic, --language arabic
                        [INFO] Language for the characters, eg: arabic -- defaults to standard
  -fs 19, --font-size 19
                        [INFO] Font size for unicode, cyrillic and arabic languages only.
  -sw 2, --stroke-width 2
                        [INFO] The value for the width of the text stroke
  -nc yes, --no-color yes
                        [INFO] User original rgb colors

```

#### swapper practical example

Process all images on images directory with a scale factor of 19, character width of 15, character height of 19, the color white as the asciification color.
```
~$ docker run -it -e script_name=swapper \
  --mount type=bind,source=$(pwd)/src/images/,target=/src/images/ \
  --mount type=bind,source=$(pwd)/src/output/,target=/src/output/ \
  --name=art \
  --rm \
  art:latest --scale-factor=0.19 --char-width=15 --char-height=19 --color 255 255 255
```
