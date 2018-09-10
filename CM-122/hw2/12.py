#!/usr/bin/python
import sys

def hammingdis (str1, str2):
	count = 0
	size = len(str1)
	for i in range (size):
		if str1[i] != str2[i]:
			count += 1
	return count


if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		pattern = f.readline().strip()
		text = f.readline().strip()
		d = int(f.readline().strip())
		position = []
		last = len(text) - len(pattern)
		for x in range (0, last):
			if hammingdis (pattern, text[x:x+len(text)]) <= d:
				position.append(x)

		print " ".join(str(element) for element in position)