#!/bin/bash

if [ ! -d ./src/images ]; then
    echo "[!] --------------------------------------------------"
    echo "[!] Making images directory at ./src/images"
    echo "[!] Images that you pass as arguments must live there."
    echo "[!] --------------------------------------------------"
    mkdir -p ./src/images;
    echo "[!] Done"
fi;

if [ ! -d ./src/output ]; then
    echo "[!] --------------------------------------------------"
    echo "[!] Making output directory at ./src/output"
    echo "[!] Ascii generated images will be outputed there."
    echo "[!] --------------------------------------------------"
    mkdir -p ./src/output;
    echo "[!] Done"
fi;

echo "[!]Building image .. python dependecies take 3-5 min (numpy)"

docker build --tag=art:latest .
