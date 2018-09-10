#!/usr/bin/python
import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		string1 = f.readline().strip()
		string2 = f.readline().strip()
		#print string1
		#print string2

		def distance(string1, string2, m, n):
			memo = [[0 for i in range(n+1)] for j in range (m+1)]

			for i in range(m+1):
				for j in range(n+1):
					if i == 0:
						memo[i][j] = j

					elif j == 0:
						memo[i][j] = i

					elif string1[i-1] == string2[j-1]:
						memo[i][j] = memo[i-1][j-1]

					else:
						memo[i][j] = 1 + min(memo[i][j-1], memo[i-1][j], memo[i-1][j-1])
			return memo[m][n]


		size1 = len(string1)
		size2 = len(string2)

		print distance(string1, string2, size1, size2)