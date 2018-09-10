import sys
import math

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		raw = f.readlines()
    	genome = raw[0].strip()
    	A = raw[1].strip().split()
    	arr = []
    	for i in A:
    		arr.append(float(i))

    	logs = []
    	for x in arr:
    		log = 0
    		for c in genome:
    			if c in "GC":
    				log += math.log(x/2,10)
    			else:
    				log += math.log((1-x)/2, 10)
    		logs.append(log)

    	print " ".join(str(ele) for ele in logs)