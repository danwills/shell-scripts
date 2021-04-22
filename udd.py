#!/usr/bin/env python
# Despite it being a bit horrible because of needing a temp-file, this is the most
# reliable way I've found to make this work, make sure this file is in the path 
# and then alias it like so:
# alias udd="udd.py > ~/tmp/udd ; source ~/tmp/udd"
# There must be another way (in zsh? for sure!)
import os

cwd = os.getcwd()
rmdir = cwd.split("/")[-1]
print("cd .. ; rmdir \"" + rmdir + "\"")
