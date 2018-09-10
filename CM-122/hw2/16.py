#!/usr/bin/python
import sys

def reverse(g):
	g_r = g[::-1]
	g_r = g_r.replace('A', 'a')
	g_r = g_r.replace('T', 'A')
	g_r = g_r.replace('a', 'T')
	g_r = g_r.replace('C', 'c')
	g_r = g_r.replace('G', 'C')
	g_r = g_r.replace('c', 'G')
	return g_r

def hammingdis (str1, str2):
	count = 0
	size = len(str1)
	for i in range (size):
		if str1[i] != str2[i]:
			count += 1
	return count

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

		dictionary = {}
		for gene in parser:
			if gene in dictionary:
				dictionary[gene] += 1
			else:
				dictionary[gene] = 1

		correct = []
		incorrect = []
		for g in dictionary:
			if dictionary[g] >= 2:
				correct.append(g)
			elif dictionary[g] == 1:
				incorrect.append(g)

		for g in incorrect:
			g_r = reverse(g)
			if g_r in correct:
				correct.append(g)
				incorrect.remove(g)

		gin = []
		gout = []
		for g in incorrect:
			for x in correct:
				if hammingdis(g, x) == 1:
					gin.append(g)
					gout.append(x)
					break

		for i, j in zip(gin, gout):
			print str(i) + "->" + str(j)







