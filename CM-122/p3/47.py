import sys

DIC = {
    "A" : "T",
    "C" : "G",
    "G" : "C",
    "T" : "A"
}

def reverse_and_complement(read):
    r_c = "".join(map(lambda label : DIC[label], list(read[::-1])))
    return r_c

def draw_graph(read_list):
    graph = {}
    for read in read_list:
        x, y = read[1:], read[:-1]
        if x not in graph:
            graph[x] = set()
        if y not in graph:
            graph[y] = set()
        graph[y].add(x)
    return graph

if __name__ == "__main__":
    read_list = []

    file_name = sys.argv[1]
    f = open(file_name)   
    for each_line in f:
        read_list.append(each_line.strip())

    graph = draw_graph(read_list + map(reverse_and_complement, read_list))
    for node in graph:
        size = len(graph[node])
        if size > 0:
            for x in graph[node]:
                print "(" + str(node) + "," + str(x) + ")"