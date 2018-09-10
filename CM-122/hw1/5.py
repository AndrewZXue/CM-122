#!/usr/bin/python
import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		string = f.read().strip('\n')
		output = ""
		for char in reversed(string):
			if char == 'A':
				output+="T"
			if char == 'C':
				output+="G"
			if char == 'G':
				output+="C"
			if char == 'T':
				output+="A"
		print output