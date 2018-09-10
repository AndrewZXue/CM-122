#!/usr/bin/python
import sys

def compute(string, ch):
	return float(string.count(ch))/float(len(string))

def generate_profile(genomes):
	size = len(genomes)
	length = len(genomes[0])
	profile = [[],[],[],[]]
	strings = []
	for y in range(0, length):
		string = []
		for x in range(0, size):
			if genomes[x][y] == 'A':
				string.append('A')
			elif genomes[x][y] == 'C':
				string.append('C')
			elif genomes[x][y] == 'G':
				string.append('G')
			elif genomes[x][y] == 'T':
				string.append('T')
		strings.append(string)
	for string in strings:
		a = compute(string, 'A')
		c = compute(string, 'C')
		g = compute(string, 'G')
		t = compute(string, 'T')
		profile[0].append(a)
		profile[1].append(c)
		profile[2].append(g)
		profile[3].append(t)
	return profile

def generate_concensus(genomes):
	size = len(genomes)
	length = len(genomes[0])
	profile = [[],[],[],[]]
	strings = []
	for y in range(0, length):
		string = []
		for x in range(0, size):
			if genomes[x][y] == 'A':
				string.append('A')
			elif genomes[x][y] == 'C':
				string.append('C')
			elif genomes[x][y] == 'G':
				string.append('G')
			elif genomes[x][y] == 'T':
				string.append('T')
		strings.append(string)
	concensus = []
	for string in strings:
		a = string.count('A')
		c = string.count('C')
		g = string.count('G')
		t = string.count('T')
		occurence = []
		occurence.append(a)
		occurence.append(c)
		occurence.append(g)
		occurence.append(t)
		if a == max(occurence):
			concensus.append('A')
		elif c == max(occurence):
			concensus.append('C')
		elif g == max(occurence):
			concensus.append('G')
		elif t == max(occurence):
			concensus.append('T')
	return concensus


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

def generate_kmer(text, k, profile):
	size = len(text)
	count = len(profile)

	max_p = 0
	kmer = text[0: k]
	for x in range(0, size - k + 1):
		p = probability(profile, text[x:x+k], k)
		if p > max_p:
			max_p = p
			kmer = text[x:x+k]
	return kmer

def score(motifs, k):
	concensus = generate_concensus(motifs)
	score = 0
	for motif in motifs:
		for i in range(0, k):
			if motif[i] == concensus[i]:
				score += 1
	return score

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		line1 = f.readline().strip().split(' ')
		k = int(line1[0])
		t = int(line1[1])
		dnas = f.read().strip().split('\n')
		length = len(dnas[0])

		best_motifs = []
		best_score = 0
		for i in range(0, length - k + 1):
			motif_1 = dnas[0][i : i+k]
			motifs = []
			motifs.append(motif_1)
			for x in range(1, t):
				profile = generate_profile(motifs)
				motifs.append(generate_kmer(dnas[x], k, profile))

			curr_score = score(motifs, k)
			if curr_score > best_score:
				best_score = curr_score
				best_motifs = motifs

		print "\n".join(str(element) for element in best_motifs)
