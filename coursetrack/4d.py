import sys
import itertools
import operator

def match(st1,st2):
	assert len(st1) == len(st2)
	return st1[1::] == st2[0:len(st2)-1]

graph = dict()


for line in sys.stdin:
	line = line.rstrip()
	a = line[0:len(line)-1]
	b = line[1:len(line)]
	if a not in graph:
		graph[a] = []
	graph[a].append(b)


				
for key in graph:
	print key + " -> " + ",".join(graph[key])