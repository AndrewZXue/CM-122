#!/usr/bin/python
import sys

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

		for graph in graphs:
			stats = graph[0].split(" ")
			num_v = int(stats[0])
			num_e = int(stats[1])
			graph = graph[1:]

			indegree = {}
			for i in range(0, num_v):
				indegree[i+1] = 0
			for ver in graph:
				vertex = ver.split(" ")
				v1 = int(vertex[0])
				v2 = int(vertex[1])
				indegree[v2] += 1
			#print indegree

			path = []
			while indegree:
				queue = []
				for key in indegree:
					if indegree[key] == 0:
						queue.append(key)
						
				for key in queue:
					del indegree[key]
					for ver in graph:
						vertex = ver.split(" ")
						v1 = int(vertex[0])
						v2 = int(vertex[1])
						if v1 == key:
							indegree[v2] -= 1
					path.append(key)
					#print indegree
			#print path
			check = True
			if not len(path) == num_v:
				check = False

			edges = []
			for ver in graph:
				vertex = ver.split(" ")
				new_vertex = map(int, vertex)
				edges.append(new_vertex)
			#print edges

			for i in range(0, len(path) - 1):
				temp = [path[i]]
				temp.append(path[i+1])
				if temp not in edges:
					check = False

			if check == True:
				print'1' + ' ' + ' '.join(map(str, path))
			else:
				print '-1'



				