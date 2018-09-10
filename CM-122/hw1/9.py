import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		strings = f.read().strip('\n').split()
		k = float(strings[0])
		m = float(strings[1])
		n = float(strings[2])

		t = k + m + n

		p = k/t + m/t * k/(t-1) + m/t * (m-1)/(t-1) * 3/4 + m/t * n/(t-1) * 1/2 + n/t * k/(t-1) + n/t * m/(t-1) * 1/2

		print p