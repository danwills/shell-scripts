#!/usr/bin/env python

import os

cwd = os.getcwd()
rmdir = cwd.split("/")[-1]
print("cd .. ; rmdir \"" + rmdir + "\"")
