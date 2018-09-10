import sys

if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name) as f:
    	string = f.readline().strip()
    	matrix = []
    	size = len(string)
    	for i in range(0, size):
    		entry = string[i:] + string[0:i]
    		matrix.append(entry)

    	sorted_matrix = sorted(matrix)
    	ret = ""
    	for x in sorted_matrix:
    		ret += x[-1]

    	print ret