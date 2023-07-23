#!/bin/bash
args_array=("$@")
for i in "${args_array[@]}"
do
  :
  echo "running with variable: $i"
done

if [ -z "$script_name" ]; then
    echo "script_name is NOT configured, Script will exit !"
    exit 
else
    echo "script_name passed is: '$script_name'"
    case ${script_name} in
    'image_segmentation')
        cd /src/bin && python3 image_segmentation "$@"
    ;;
    'swapper')
        cd /src/bin && python3 swapper "$@"
    ;;
    'make_gif')
        cd /src/bin && python3 make_gif "$@"
    ;;
  esac 
 fi
