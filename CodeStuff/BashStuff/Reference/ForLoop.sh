#!/bin/bash
arrayToIndexThrough=(1 2 4 8 16 32 64 128)
for i in array ${arrayToIndexThrough[@]}
	do
	echo "$i"
done