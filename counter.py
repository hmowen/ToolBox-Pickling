""" A program that stores and updates a counter using a Python pickle file"""

from os.path import exists
import sys
import os
from pickle import dump, load
import pickle
#from pattern.web import *

def update_counter(file_name, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
	"""
# ts_eliot_texts_FULL = URL('http://www.gutenberg.org/cache/epub/1567/pg1567.txt').download()
# f = open('ts_eliot_full.pickle','w')
# pickle.dump(ts_eliot_texts_FULL,f)
# f.close()
# input_file = open('ts_eliot_full.pickle','r')
# reloaded_copy_of_eliot_texts = pickle.load(input_file)
	if os.path.exists(file_name) == False:
		f = open(file_name, 'w')
		counter = 1
		pickle.dump(counter, f)
		f.close
		return counter

	elif os.path.exists(file_name) == True:
		if reset == True:
			f = open(file_name, 'w')
			counter = 1
			pickle.dump(counter, f)
			f.close
			return counter

		else:
			f = open(file_name, 'r+')
			counter = pickle.load(f)
			counter += 1
			f.seek(0,0)
			pickle.dump(counter, f)
			f.close
			return counter

	print counter




# # Save data to a file (will be part of your data fetching script)
# lincoln_speeches_FULL = URL('http://www.gutenberg.org/cache/epub/14721/pg14721.txt').download()
# f = open('lincoln_speeches.pickle','w')
# pickle.dump(lincoln_speeches_FULL,f)
# f.close()


if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))