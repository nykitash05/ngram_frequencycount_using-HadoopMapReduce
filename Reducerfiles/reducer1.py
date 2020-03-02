#!/usr/bin/env python
"""reducer1.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
	line = line.strip()

    # parse the input we got from mapper.py based on tab
	word = line.split('\t')
        try:
             word[1] = int(word[1])
        except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
             continue
    # code operation for counting word frequency
	if current_word == word[0]:
        	current_count+= word[1]
	else:
        	if current_word:
            # write result to STDOUT
			# Clause to print only those words whose frequency are greater than 5
			if (current_count >5):
            			print current_word+'\t',current_count
        	current_count = word[1]
        	current_word = word[0]

# Output of the last word if needed!
if current_word == word[0]:
	if (current_count >5):
		print current_word +'\t',current_count
