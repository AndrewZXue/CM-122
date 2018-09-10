#!/usr/bin/python
import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	raw = []
	with open(file_name) as f:
		genome1 = f.readline().strip()
		genome2 = f.readline().strip()
		#print genome1
		#print genome2
		size1 = len(genome1)
		size2 = len(genome2)


		def lcs(X , Y):

			m = len(X)
			n = len(Y)
			L = [[None]*(n+1) for i in xrange(m+1)]
			S = [[None]*(n+1) for i in xrange(m+1)]

			for i in range(m+1):
				for j in range(n+1):
					if i == 0 or j == 0 :
						L[i][j] = 0
						S[i][j] = []
					elif X[i-1] == Y[j-1]:
						L[i][j] = L[i-1][j-1]+1
						S[i][j] = S[i-1][j-1]+list(X[i-1])
					else:
						L[i][j] = max(L[i-1][j] , L[i][j-1])
						if L[i-1][j] > L[i][j-1]:
							S[i][j] = S[i-1][j]
						else:
							S[i][j] = S[i][j-1]
			return S[m][n]

       	# def longest_substring(X, Y, m, n):
       	# 	if m == 0 or n == 0:
       	# 		return []
       	# 	elif X[m-1] == Y[n-1]:
       	# 		return longest_substring(X, Y, m-1, n-1) + list(X[m-1])
       	# 	else:
       	# 		option1 = longest_substring(X, Y, m, n-1)
       	# 		option2 = longest_substring(X, Y, m-1, n)
       	# 		if len(option1) > len(option2):
       	# 			return option1
       	# 		else:
       	# 			return option2

       	substring = lcs(genome1, genome2)

      	print "".join(element for element in substring)


