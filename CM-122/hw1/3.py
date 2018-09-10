#!/usr/bin/python
import sys
from string import maketrans

if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name) as f:
		words=[]
		count=[]
		dictionary={}
		words=f.read().strip('\n').split(' ')

		for word in words:
			count.append(words.count(word))
  
		for i in range(0,len(words)):
			dictionary[words[i]]=count[i]

		for word, num in dictionary.items():
			print word, num