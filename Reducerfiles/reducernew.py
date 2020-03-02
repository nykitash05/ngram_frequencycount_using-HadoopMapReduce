#!/usr/bin/env python
"""reducer1.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
mylistforword = []
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
            # Store result in a 2D- list
			mylistforword.append([current_word,int(current_count)])
        	current_count = word[1]
        	current_word = word[0]

# Output of the last word if needed!
if current_word == word[0]:
		mylistforword.append([current_word,int(current_count)])

#Code to print top 100 words
mylistforword.sort(key=itemgetter(1))
print(list(reversed(mylistforword[-100:])))
