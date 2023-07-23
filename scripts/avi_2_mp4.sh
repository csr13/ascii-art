#!/bin/bash

function usage() {
    echo "[ERROR] Missing arguments.";
    echo "[USAGE] => /bin/bash avi_2_mp4.sh <avi file on output dir> <desired mp4 output filename>";
}


if [ ! $(which ffmpeg) ];then
    echo "[INFO] Install ffmpeg";
    exit 1;
fi;

if [ $# -ne 2 ];then
    usage
    exit 1
fi;

out_dir="$(pwd)/output"
avi="$out_dir/$1"
mp4="$out_dir/$2"

if [ -f $avi ]; then
    echo "[INFO] $avi found ... converting";
else
    echo "[INFO] $avi not found on $out_dir";
fi

ffmpeg -i $avi -c:v libx264 \
    -flags:v "+cgop" \
    -g 15 \
    -bf 1 \
    -coder ac \
    -profile:v high \
    -crf 25 \
    -pix_fmt yuv420p \
    -c:a aac \
    -strict -2 \
    -b:a 384k \
    -r:a 48000 \
    -movflags faststart \
    $mp4
