import sys

def matcher (str1, str2):
	size = len(str1)
	for i in range (size):
		if str1[i] != str2[i]:
			return 0
	return 1

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		genome = f.readline().strip()
		parameters = f.read().strip().split(' ')
		k = int(parameters[0])
		L = int(parameters[1])
		t = int(parameters[2])

		k_mer = []

		size = len(genome)
		for i in range (size - k):
			count = 0
			str1 = genome[i:i+k]
			for x in range (i, min(i+L-k, size - k)):
				str2 = genome[x:x+k]
				count += matcher(str1, str2)

			if (count >= t and str1 not in k_mer):
				k_mer.append(str1)

		print " ".join(str(element) for element in k_mer)