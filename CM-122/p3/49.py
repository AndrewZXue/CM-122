import sys

GENES = "ATGC"
COMPLEMENT = {"A":"T","T":"A","G":"C","C":"G"}

def reverse_c(dna):
    ret = ""
    for i in range(0, len(dna)):
        ret = COMPLEMENT[dna[i]] + ret
    return ret

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		dnas = [x.strip() for x in f.readlines()]

		for x in reversed(range(2,len(dnas[0])+1)):
			mers = set()
			for dna in dnas:
			    for i in range(len(dna)-x+1):
			        mers.add(dna[i:i+x])
			        mers.add(reverse_c(dna[i:i+x]))

			ret = None
			stack = []
			stack.append(([],set()))

			while len(stack) > 0 and ret == None:
			    path,vs = stack.pop()

			    if len(path) == 0:
			        for mer in mers:
			            stack.append(([mer],set([mer])))
			    else:
			        mer = path[-1]
			        for a in GENES:
			            nmer = mer[1:] + a		       
			            if nmer in mers and nmer != reverse_c(mer):
			                if nmer == path[0]:
			                    ret = list(path)
			                    break
			                elif not nmer in vs:
			                    stack.append((path + [nmer],vs.union(set([nmer]))))

			if ret != None:
			    output = ret[0]
			  
			    for i in range(1, len(ret)):
			        output += ret[i][-1]
			        
			    output = output[:-(x-1)]
			    doutput = output + output
			    success = True
			    
			    for dna in dnas:
			        if doutput.find(dna) == -1 and doutput.find(reverse_c(dna)) == -1:
			            success = False

			    if success:
			        print output
			        break