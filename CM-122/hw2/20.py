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

		genome = parser[1]


		size = len(genome)
		P_array = []
		for i in range(size):
			P_array.append(0)

		j = 0

		for k in range (2, size):
			while j > 0 and genome[j] != genome[k - 1]:
				j = P_array[j - 1]
			if genome[j] == genome[k - 1]:
				j = j + 1
			P_array[k - 1] = j

		print " ".join(str(element) for element in P_array)