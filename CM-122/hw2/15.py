#!/usr/bin/python
import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	raw = []
	with open(file_name) as f:
		raw = f.read().split('>')
		parser = []
		for line in raw:
			line = line[14:].replace('\n', '')
			parser.append(line)

		parser = parser[1:]
    	size = len(parser)
    	length = len(parser[0])
    	A = []
    	C = []
    	G = []
    	T = []
    	string = []

    	for x in range (length):
    		a_temp = 0
    		c_temp = 0
    		g_temp = 0
    		t_temp = 0
    		for y in range (size):
    			c = parser[y][x]
    			if c == 'A':
    				a_temp += 1
    			if c == 'C':
    				c_temp += 1
    			if c == 'G':
    				g_temp += 1
    			if c == 'T':
    				t_temp += 1
    		maximum = max(a_temp, c_temp, g_temp, t_temp)
    		str_temp = ''
    		if a_temp == maximum:
    			str_temp = 'A'
    		elif c_temp == maximum:
    			str_temp = 'C'
    		elif g_temp == maximum:
    			str_temp = 'G'
    		elif t_temp == maximum:
    			str_temp = 'T'

    		A.append(a_temp)
    		C.append(c_temp)
    		G.append(g_temp)
    		T.append(t_temp)
    		string.append(str_temp)

    	print ''.join(element for element in string)
    	print "A: " + " ".join(str(num) for num in A)
    	print "C: " + " ".join(str(num) for num in C)
    	print "G: " + " ".join(str(num) for num in G)
    	print "T: " + " ".join(str(num) for num in T)



