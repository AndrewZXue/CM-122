#!/usr/bin/python
import sys
import numpy as np

def hamm_rate (str1, str2):
	count = 0
	size = len(str1)
	for i in range(0, size):
		if str1[i] != str2[i]:
			count += 1
	rate = float(count)/float(size)
	return rate

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
		matrix = np.zeros((size, size), dtype=np.float)

		for i in range(0, size):
			for j in range(0, size):
				matrix[i][j] = hamm_rate(parser[i], parser[j])

		np.savetxt(sys.stdout, matrix, fmt="%.5f")