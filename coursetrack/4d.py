import sys
import itertools
import operator

def match(st1,st2):
	assert len(st1) == len(st2)
	return st1[1::] == st2[0:len(st2)-1]

patterns = set()
k = 0
for line in sys.stdin:
	line = line.rstrip()
	k = len(line)-1
	for i in range(0, len(line) - k + 1):
		patterns.add( line[i:i+k] )

graph = dict()

patterns = list(patterns)
print patterns
	
for i in range(0, len(patterns)):
	for j in range(0, len(patterns)):
		if i == j:
			continue
		else:
			if match(patterns[i], patterns[j]):
				if patterns[i] not in graph:
					graph[ patterns[i] ] = set()
				graph[ patterns[i] ].add( patterns[j] )
				
for key in graph:
	print key + " -> " + ",".join(graph[key])