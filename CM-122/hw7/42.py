import sys

if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name) as f:
    	string = f.readline().strip()
    	string_list = f.read().split('\n')

    	pos = []
    	length = len(string_list[0])
    	
    	for i in range(len(string)):
    		str2 = string[i:i+length]
    		for str1 in string_list:
    			if (str1 == str2):
    				pos.append(i)

    	print " ".join(str(i) for i in pos)
    