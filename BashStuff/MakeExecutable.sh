#!/bin/bash
find . -name '*.sh' -exec sudo chmod +x {} \;
find ../NAS -name '*.sh' -exec sudo chmod +x {} \;
#find ..