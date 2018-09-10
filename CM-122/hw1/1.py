#!/usr/bin/python
import sys

if __name__ == "__main__":
    file_name = sys.argv[1]
    with open(file_name) as f:
        text, text_index = f.readlines()
        text_i = text_index.split(" ")
        a,b,c,d = map(int,text_i)
    print text[a:b+1], text[c:d+1]