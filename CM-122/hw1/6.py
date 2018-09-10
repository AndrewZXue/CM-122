#!/usr/bin/python
import sys

def rec(n, k):
	if  (n == 1 or n == 2):
		return 1
	return (k * rec(n-2, k) + rec(n-1, k))

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		arguments = f.read().strip('\n').split(' ')
		month = int(arguments[0])
		rate = int(arguments[1])
		print rec(month, rate)