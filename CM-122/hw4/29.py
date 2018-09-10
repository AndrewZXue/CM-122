#!/usr/bin/python
import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		const = f.readline().strip()
		edges = f.read().strip().split('\n')
		const_2 = const.split(" ")
		num_v = int(const_2[0])
		num_e = int(const_2[1])
		print num_v

		list = [0] * num_v
		print list
		for edge in edges:
			edge_v = edge.split(" ")
			print edge_v
			list[int(edge_v[0]) - 1] += 1
			list[int(edge_v[1]) - 1] += 1

		print " ".join(str(element) for element in list)