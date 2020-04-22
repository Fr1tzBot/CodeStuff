#!/bin/bash
#Index through an array
arrayToIndexThrough=(1 2 4 8 16 32 64 128)
for i in array ${arrayToIndexThrough[@]}
	do
	echo "$i"
done
#Repeat a set number of times (10)
for i in {1..10}
	do
	echo i
	break
done