#!/bin/bash
gcc -pedantic -Wall -Wextra -O1 -fsanitize=address hidraw-haptic.c -o hidraw-haptic.o
