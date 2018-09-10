import sys

def Motzkin(rna):
	if len(rna) <= 1:
		return 1

	else:
		if rna in d:
			return d[rna]
		else:
			sub = []
			size = len(rna)
			for i in range(1, size):
				if rna[0] == dictionary[rna[i]]:
					sub.append([rna[1:i],rna[i+1:]])

			d[rna] =  (sum([Motzkin(x[0])*Motzkin(x[1]) for x in sub]) + Motzkin(rna[1:])) % 1000000
			
			return d[rna]





if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name) as f:
    	f.readline()
    	raw = f.read()
    	rna = raw.replace('\n', '')

    	dictionary = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
    	d = {}
    	print Motzkin(rna)


