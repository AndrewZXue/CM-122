import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		strings = f.read().strip('\n').split()
		first = strings[0]
		second = strings[1]

		length = len(first)
		distance = 0

		for x in range(0, length):
			if first[x] != second[x]:
				distance += 1

		print distance