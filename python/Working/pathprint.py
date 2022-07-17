#!/usr/bin/env python
import sys,os
for i in (os.getenv("PATH") if len(sys.argv)<=1 else sys.argv[-1]).split(":"):print(i)