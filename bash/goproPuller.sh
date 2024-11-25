#!/bin/bash

outdir="./"
indir="./"

# parse args with $# and shift
while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help)
        echo "Usage: $0 [options] [arguments]"
        echo "Options:"
        echo "  -h, --help  Show this help message and exit"
        echo "  -d, --dir   Directory to pull files from"
        echo "  -o, --out   Directory to save files to"
        exit 0
        ;;
        -d|--dir)
            shift
            indir=$1
        ;;
        -o|--out)
            shift
            outdir=$1
        ;;
        *)
            echo "Unknown option: $1"
            exit 1
        ;;
    esac
        shift
done

# throw a fit if indir == outdir
if [ "$indir" == "$outdir" ]; then
    echo "Input and output directories cannot be the same"
    exit 1
fi
IFS=$'\n'
names=$(find "$indir" -name "*.MP4" | sed "s/\.MP4//")

for (( i=0; i<${#names[@]}; i++ )); do
    name=${names[i]}
    echo "Processing $name"
    ffmpeg -i "$name.MP4" -i "$name.THM" -map 0 -map 1 -c copy -disposition:v:1 attached_pic "$outdir/$name.MP4"

done