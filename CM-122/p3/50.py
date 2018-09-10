import sys

def asmq(strings,N=50):
    return asmq_helper([len(s) for s in strings],N)

def asmq_helper(strings,N):
    strings.sort()
    total = sum(s for s in strings)
    target = N * total / 100
    indicator = 0
    size = len(strings) - 1
    while indicator < target:
        indicator += strings[size]
        size = size - 1
    return strings[size+1]

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		strings = f.read().strip().split("\n")
		#print strings
		print asmq(strings),asmq(strings,N=75)
