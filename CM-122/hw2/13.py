#!/usr/bin/python
import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		genome = f.readline().strip()
		mini = 0
		C = 0
		G = 0
		position = []
		size = len(genome)
		for i in range (size):
			if genome[i] == 'C':
				C += 1
			if genome[i] == 'G':
				G += 1
			skew = G - C
			if skew < mini:
				mini = skew
				position = [i+1]
			elif skew == mini:
				position.append(i+1)

		print " ".join(str(element) for element in position )