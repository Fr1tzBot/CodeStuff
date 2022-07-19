from ast import arg
import os
from sys import argv
from typing import Iterator #too lazy to use argparse, so bash-like argument parsing

#this is repetitive and shit but works
argv = argv[1:]
while len(argv) > 0:
    match argv[0]:
        case "--source":
            source = argv[1]
            argv = argv[2:]
        case "-s":
            source = argv[1]
            argv = argv[2:]
        case "--dest":
            dest = argv[1]
            argv = argv[2:]
        case "-d":
            dest = argv[1]
            argv = argv[2:]

for (dirpath, dirnames, filenames) in os.walk(source):
    print(dirpath)
    print(dirnames)
    print(filenames)
    print("\n")