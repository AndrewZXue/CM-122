#!/usr/bin/python
import sys

def dfs (dictionary, v, vs):
	if sum(vs) == len(vs):
		return [-2]
	if v not in dictionary.keys():
		return [-1]
	else:
		map_v = dictionary[v]
		for x in map_v:
			if vs[x-1] == 1:
				continue
			else:
				vs[x-1] = 1
			next_p = dfs(dictionary, x, vs)
			if next_p == [-1]:
				vs[x-1] = 0
				continue
			else:
				return [x] + next_p
		return [-1]

def readraw(raw, graphs):
	if len(raw) == 0:
		return None
	stat = raw[0].split(" ")
	num_lines = int(stat[1])
	graphs.append(raw[0:num_lines+1])
	graphs.append(readraw(raw[num_lines+1:], graphs))
	return graphs

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		num_g = int(f.readline().strip())
		graphs = []
		raw = f.read().strip().split("\n")
		#print raw
		raw_graphs = readraw(raw, graphs)
		graphs = raw_graphs[0:num_g]
		#print graphs
		#print graphs
		
		for graph in graphs:
			stats = graph[0].split(" ")
			num_v = int(stats[0])
			num_e = int(stats[1])
			edges = graph[1:]
			dictionary = {}

			for edge in edges:
				vertex = edge.split(" ")
				v1 = int(vertex[0])
				v2 = int(vertex[1])
				if v1 not in dictionary.keys():
					dictionary[v1] = [v2]
				else:
					dictionary[v1].append(v2)

			print dictionary
			
	
			vs = [0]*num_v
			#print vs
			vertices = edges[0].split(" ")
			starting_v = int(vertices[0])
			vs[starting_v - 1] = 1
			array = [starting_v] + dfs(dictionary, starting_v, vs)
			#print vs
			if array[1] == -1:
				print -1
			else:
				print str(1) + " " +" ".join(str(k) for k in map(str, array[0:num_v]))


