import sys

if __name__ == "__main__":
	file_name = sys.argv[1]
	with open(file_name) as f:
		k_mers = []
		for line in f:
			k_mers.append(line.strip())
	edge_node = set()
	for x in k_mers:
		edge_node.add(x)
	form_edge = lambda node: [node[:-1], node[1:]]
	edges = []
	for key in edge_node:
		edges.append(form_edge(key))


	curr = edges.pop(0)
	ret = curr[0][-1]
	while edges:
		ret += curr[1][-1]
		[i] = [x for x, y in enumerate(edges) if y[0] == curr[1]]
		curr = edges.pop(i)
	print ret
