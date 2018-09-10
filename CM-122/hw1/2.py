#!/usr/bin/python
import sys

if __name__ == "__main__":
    file_name = sys.argv[1]
    i = 1
    with open(file_name) as f:
    	for line in f.readlines():
    		if i % 2 == 0:
    			print line
    		i = i + 1