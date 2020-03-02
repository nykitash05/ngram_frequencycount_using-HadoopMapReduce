#!/usr/bin/env python
"""mapper.py"""

import sys,re
import string
# input comes from STDIN (standard input)
for line in sys.stdin:
	if not line:
		break
        if len(line) > 1:
	        # remove the starting and trailing whitespace
		line = line.strip()
        	# split the line into words
		words = line.split()
        	#Printing key and value pairs to be sent to reducer.py
        	for word in words:
			#Code for data cleaning
		  	word = word.lower()
			word = re.sub(r'[^\w\s]','',word)
			words = list(filter(None,words))
			if (re.match('^(?=.*[0-9]$)|(?=.*[a-zA-Z])', word)):
				#Print all the relevant words
				print word+'\t',1
