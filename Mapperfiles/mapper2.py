#!/usr/bin/env python
"""mapper.py"""

import sys,re
import string
varstart = None
varend = None
varlist =[]
# input comes from STDIN (standard input)
for line in sys.stdin:
	if not line:
		break
        if len(line) > 1:
		# remove leading and trailing whitespace
		line = line.strip()
		# split the line into words
		words = line.split()
		#Data cleansing
		words = [x.lower() for x in words]
		words = list(re.sub(r'[^\w\s]','',x) for x in words)
		words = list(filter(None,words))
		if (re.match('^(?=.*[0-9]$)|^(?=.*[a-zA-Z])',x) for x in words):
		#Printing key(bigrams) and value pairs to be sent to reducer2.py
			for i in range(len(words)-1):
				print str(words[i:i+2])+'\t',1
				if (i == 0):
					varstart = words[i]
				if (i== (len(words)-2)):
					varend = words[i+1]
					varlist.append([varstart,varend])

#Print all the bigrams created from last word,first word of consecutive lines
for i in range(len(varlist)-1):
		print str([varlist[i][1],varlist[i+1][0]]) +'\t',1
