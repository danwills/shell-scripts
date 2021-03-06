#!/usr/bin/env python2
# 
# sxd - Super xd
# 	A super lazy cd that searches back along the path for matches, then if a match is found,
# continues down the other branch, as possible.
#
#   With 1 arg: uses a listing at each level to search for a match, if one is found it is selected
#	then the rest of the path is matched up as far as possible.
#   	
#   With 2 or more args - it tries to match all of them - sometimes a bit unpredictable in this mode..
#
#   Not implemented yet:
#	With an arg formatted like a=b, the path is searched for the first part and then replaced with the second,
#	then the rest of the path is lazily matched
#
# Example (zsh) alias:
#    alias xd="cd `sxd.py $@`"
#
# Dan Wills - gdanzo@gmail.com

import os
debug = True
try :
	import sys, string, glob

	debug = False

	if "-d" in sys.argv :
		debug = True
		print( "#  debug mode ON! ")
		print( "#  " + os.getcwd() + " ; ")

	def getNumMatches( instr, names, separator ) :
		count = 0
		for s in string.split( instr, separator ) :
			if s in names :
				count += 1
		return count

	def stripLastSlash( instr ) :
		if instr :
			if len( instr ) > 2 :
				if instr[-1] == "/" :
					return instr[:-1]
				else : return instr
			else : return instr

	if (len(sys.argv) >= 2) :

		src = sys.argv[1:]
		
		if (debug) : print "#  src: " + str(src)

		originalpath = os.getcwd()
		originalsplit = string.split( originalpath,"/")
		rollpath = os.getcwd()
		rollsplit = string.split( rollpath,"/")
		rolllen = len(rollsplit)

		wasInInitialDir = None

		bestmatchlength = 0
		bestnummatches = 0

		for argk in range( 0, len( src ), 1) :
			arg = src[argk]
			if arg != "-d" : 
				for x in range( rolllen - 1, -1, -1 ) :

					listpath = string.join( rollsplit[:x+1], "/" ) + "/"
					therest = string.join( rollsplit[x+2:], "/" )

					filePattern = listpath + '*'
					
					if (debug) : print "#  index: " + str(x)
					if (debug) : print "#  searching: " + filePattern + " for: " + arg.strip("/")

					fileList = glob.glob( filePattern )
					fileList.sort()

					for f in fileList :
						if os.path.isdir(f) :
							matchsplit = string.split(f,"/")
							if ( debug ) : print "# considering: " + matchsplit[-1]

							if ( matchsplit[-1] == arg.strip("/") ) or ( arg.strip("/") in matchsplit[-1] ) :
								if ( debug ) : print "#  found target           " + f
								if ( debug ) : print "#  therest is:            " + therest 
								
								if x == (rolllen - 1) : 
									if rollpath == originalpath :
										if ( debug ) : print "# found target in initial dir: " + f
										wasInInitialDir = f
									else :
										if ( debug ) : print "# found target on branch " + f
										rollpath = f

								rang = range( x+2, rolllen+1 )
								rang.reverse()
								
								for z in rang :
									j = f + "/" + string.join( rollsplit[x+2:z], "/" )
									if j != originalpath :
										if ( debug ) : print "#  checking dir : " + j

										if os.path.isdir( j ) :
											if ( debug ) : print "#  dir exists! " + j

											matchlength = len( string.split( j, "/") )

											if ( debug ) : print "#  matchlength " + str( matchlength )

											if matchlength > bestmatchlength :
												if ( debug ) : print "#  -----------------------------dir is bigger than best match so far " + str( matchlength )
												rollpath = j
												bestmatchlength = matchlength
				rollsplit = string.split( rollpath, "/" )
				rolllen = len( rollsplit )
		
		if wasInInitialDir : 
			# if we went nowhere.. might as well try a normal 'cd'
			if stripLastSlash( rollpath ) == stripLastSlash( originalpath ) :
				if ( debug ) : print "# going with cd in initial dir"
				rollpath = wasInInitialDir
				wasInInitialDir = None
				
			else :
				if ( debug ) : print "# lenroll: " + str( len( stripLastSlash( rollpath ).split("/") ) )
				if ( debug ) : print "# lenorig: " + str( len( stripLastSlash( originalpath ).split("/") ) )
				
				if len( stripLastSlash( rollpath ).split("/") ) >= len( stripLastSlash( originalpath ).split("/") ) :
					if ( debug ) : print "# going with cd into better (longer) branch match"
					rollpath = wasInInitialDir
					wasInInitialDir = None
		
		if ( debug ) : print("#  RESULT:")
		if ( debug ) : 
			print( "#  " + rollpath )
		else : print rollpath
except:
	if ( debug ) : 
		print("Exception caught! ")
		raise
	print os.getcwd()
	
