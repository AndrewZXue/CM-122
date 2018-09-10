#!/usr/bin/python
import sys

if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name) as f:
    	kmers = f.read().strip().split('\n')
    	k = len(kmers[0])
    	paths = []
    	for start in kmers:
    		for desti in kmers:
    			if start[1:k] == desti[0:k-1]:
    				path = start + " -> " + desti
    				if path not in paths:
    					paths.append(path)
    	paths.sort()
    	print '\n'.join(str(element) for element in paths)


    		