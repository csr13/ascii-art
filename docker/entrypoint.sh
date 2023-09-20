#!/bin/sh

args_array=$@

if [ -z "$script_name" ]; then
    echo "script_name is NOT configured, Script will exit !"
    exit 
else
    echo "script_name passed is: '$script_name'"
    case ${script_name} in
    'image_segmentation')
        cd bin && python3 image_segmentation $@
    ;;
    'swapper')
        cd bin && python3 swapper $@
    ;;
    'make_gif')
        cd bin && python3 make_gif $@
    ;;
  esac 
 fi
