#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()

    # parse the input we got from mapper.py
	word = line.split('\t')
        try:
             word[1] = int(word[1])
        except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
             continue
	#Code for counting
	if current_word == word[0]:
        	current_count+= word[1]
	else:
        	if current_word:
            # write result to STDOUT
			 if (current_count >5):
            			print current_word +'\t', current_count
        	current_count = word[1]
        	current_word = word[0]

# Output the last word if needed!
if current_word == word[0]:
	if (current_count >5):
		print current_word+'\t', current_count
