#!/usr/bin/python
import sys

def probability(profile, string, k):
	p = 1
	for i in range(0, k):
		if string[i] == 'A':
			p *= profile[0][i]
		elif string[i] == 'C':
			p *= profile[1][i]
		elif string[i] == 'G':
			p *= profile[2][i]
		else:
			p *= profile[3][i]
	return p

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		text = f.readline().strip()
		size = len(text)
		k = int(f.readline().strip())
		profile = f.read().strip().split('\n')
		count = len(profile)
		for i in range(0, count):
			profile[i] = map(float, profile[i].split(' '))
		
		max_p = 0
		kmer = text[0: k]
		for x in range(0, size - k + 1):
			p = probability(profile, text[x:x+k], k)
			if p > max_p:
				max_p = p
				kmer = text[x:x+k]

		print kmer

