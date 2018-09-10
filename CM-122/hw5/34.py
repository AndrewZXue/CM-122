#!/usr/bin/python
import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	raw = []
	with open(file_name) as f:
		total = int(f.readline().strip())
		change = map(int, f.readline().strip().split(","))
		size = len(change)
		change = change[::-1]

		def least_change(change, m, weight):
			memo = [None] * (weight+1)
			memo[0] = 0
			for i in range(1, (weight+1)):
				memo[i] = sys.maxsize
			for i in range(1, (weight+1)):
				for k in range(0, m):
					if (change[k] <= weight):
						sub_ret = memo[i-change[k]]
						if(sub_ret != sys.maxsize and sub_ret+1 < memo[i]):
							memo[i] = sub_ret + 1

			return memo[weight]



			# ret = sys.maxsize

			# for i in range(0, m):
			# 	if (change[i] <= weight):

			# 		sub_ret = least_change(change, m, weight-change[i])
			# 		if(sub_ret != sys.maxsize and sub_ret + 1 < ret):
			# 			ret = sub_ret + 1
			# return ret

		
		num = least_change(change, size, total)
		print num