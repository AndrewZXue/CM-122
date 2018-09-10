import sys

def rec_helper(N):
	for n in N:
		if isinstance(n, list):
			for sub_n in rec_helper(n):
				yield sub_n	
		else:
			yield n

def coverage(s, e, k):
	
	cov = [key for key, item in enumerate(e) if item[0] == s[1-k:]]

	if len(cov) == 0:
		return [s if e == [] else []]
	else:
		return [coverage(s + e[i][1][-1], e[:i] + e[i + 1:], k) for i in cov]

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		strings = f.read().strip().split("\n")
		k = len(strings[0])

		edge = lambda x: [x[0:k-1],x[1:k]]

		DBG = [edge(x) for x in strings[1:]]

		circle = [i[:len(strings)] for i in set(rec_helper(coverage(strings[0], DBG, k)))]

		for S in circle:
			print S
