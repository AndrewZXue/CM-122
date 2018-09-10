#!/usr/bin/python
import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		string = f.read().strip('\n')
		counts = [0, 0, 0, 0]
		for char in string:
			if char == 'A':
				counts[0]+=1
			if char == 'C':
				counts[1]+=1
			if char == 'G':
				counts[2]+=1
			if char == 'T':
				counts[3]+=1
		countstr = [str(counts[0]), str(counts[1]), str(counts[2]), str(counts[3])]
		print " ".join(countstr)
		