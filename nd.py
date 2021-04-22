#!/usr/bin/env python
# Support for an alias that can make and enter directories, 
# including with spaces in the name and multiple levels at once if there are slashes '/'.
# This can be aliased in zsh (bash too I hope, maybe with some translation?) as follows:
# Make sure this file is in the path, then:
#function ndir
#{
#	cd "`nd.py \"$@\"`"
#}
#alias nd=ndir

import sys
import os

args = sys.argv
if args and len(args) > 1 :
	mkdir = " ".join( args[1:] )
	pwd = os.getcwd()
	mdir = pwd + "/" + mkdir
	if mkdir[0] == "/" :
		mdir = mkdir
	if not os.path.isdir( mdir ) :
		os.makedirs( mdir )
		if os.path.isdir( mdir ) :
			print(mdir)
	else :
		print(mdir)

	
