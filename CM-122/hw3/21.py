#!/usr/bin/python
import sys
from itertools import product

def hammingdis (str1, str2):
	count = 0
	size = len(str1)
	for i in range (size):
		if str1[i] != str2[i]:
			count += 1
	return count

def generate (size):
	kmer = []
	kmer = [''.join(ch) for ch in product('ACGT',repeat=size)]
	return kmer 


if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		size = int(f.readline().strip())
		dnas = []
		dnas = f.read().strip().split('\n')
		kmer = generate(size)
		size_dna = len(dnas[0])
		count = len(dnas)
		median = dnas[0]
		min_sum = count * size
		for string in kmer:
			summ = 0
			for dna in dnas:
				min_diff = size
				for i in range(0, size_dna - size + 1):
					diff = hammingdis(string, dna[i:i+size])
					if diff <= min_diff:
						min_diff = diff
				summ += min_diff
			if summ < min_sum:
				min_sum = summ
				median = string
		print median



