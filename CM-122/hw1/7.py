#!/usr/bin/python
import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		string = f.read().strip('\n').split('>')
		dictionary = {}
		for x in string:
			if len(x) == 0:
				continue
			incident = x.split()
			label = incident[0]
			genome = ''.join(incident[1:])
			gc = 0
			percentage = 0
			for c in genome:
				if c == 'C':
					gc+=1
				if c == 'G':
					gc+=1
			percentage = (float(gc) / float(len(genome))) * 100
			dictionary[label] = percentage

	ret_label = None
	ret_per = 0
	for l, p in dictionary.iteritems():
		if p > ret_per:
			ret_per = p
			ret_label = l


	print ret_label
	print ret_per
