import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	raw = []
	with open(file_name) as f:
		data = map(float, f.readline().split(' '))

		print 2*(data[0]+data[1]+data[2]) + .75 * 2 * data[3] + .5 * 2 * data[4]
