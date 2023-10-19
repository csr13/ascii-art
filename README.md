
<h1 align="center"> Ascii Art </h1>

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<p align="center">
    <img src="./etc/anime.png"   />
</p>

A set of scripts for asciifying images, can be run locally or via docker container.

### Docker Setup (Recommended)

There is a `build.sh` script on this directory, it builds the image docker image as `art:latest` -- uses alpine.

```
~$ docker build --tag=art:latest .
```

To run the container, it is necesary to mount two bind volumes so that the ouput can be inspected on the local machine

Examples.

```
~$ docker run -it -e script_name=image_segmentation \
  --mount type=bind,source=$(pwd)/src/images/,target=/home/art/src/images/ \
  --mount type=bind,source=$(pwd)/src/output/,target=/home/art/src/output/ \
  --name=art \
  --rm \
  art:latest image_segmentation -h

~$ docker run -it -e script_name=image_segmentation \
  --mount type=bind,source=$(pwd)/src/images/,target=/home/art/src/images/ \
  --mount type=bind,source=$(pwd)/src/output/,target=/home/art/src/output/ \
  --name=art \
  --rm \
  art:latest swapper -h
```

Every script has it's help menu -- trigger it by running the script with
the --help flag, below is the output of each of the scripts

Usable Scripts:

- `image_segmentation`
- `swapper`

> ❗ It is required to pass the name of the script to use as an env variable when runing the container eg:
> 
> `~$docker ... -e script_name=<script_name>`

### image_segmentation Asciify segmented parts of image 

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

Example:

Run `image_segmentation` on an image sky.jpeg where the whites of the image will be asciified, only apply to coordenates left, upper, right, lower, apply 133 (agression for asciification) scale factor of the asciification to 0.22 character width 10 character height 10 and apply color red to asciification.
```
~$ docker run -it -e script_name=image_segmentation \
  --mount type=bind,source=$(pwd)/src/images/,target=/home/art/src/images/ \
  --mount type=bind,source=$(pwd)/src/output/,target=/home/art/src/output/ \
  --name=art \
  --rm \
  art:latest sky.jpeg white 0 0 1000 1000 133 png --scale-factor=0.22 --char-width=10 --char-height=10 --color 255 0 0
```

> :exclamation: It is important to notice that if given wrong coordinates there will be a segmentation fault, but if your give inaccurate coordinates the program will throw an exception with a informative exception message.
---


#### swapper Asciify the entire picture, image to ascii image.

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

With this script it is possible to change the color of the ascii characters, as well as using the arabic language, I included some fonts.

Process all images on images directory with a scale factor of 19, character width of 15, character height of 19, the color white as the asciification color
```
~$ docker run -it -e script_name=swapper \
  --mount type=bind,source=$(pwd)/src/images/,target=/home/art/src/images/ \
  --mount type=bind,source=$(pwd)/src/output/,target=/home/art/src/output/ \
  --name=art \
  --rm \
  art:latest --scale-factor=0.19 --char-width=15 --char-height=19 --color 255 255 255
```

<h3 align="center"> swapper output examples </h3>
<p align="center">
    <img width=350 height=350 src="./etc/anime.png"   /> <img width=350 height=350 src="./etc/swapper.png" />
</p>
