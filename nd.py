#!/usr/bin/env python

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

	
