import sys
import itertools
import operator

def match(st1,st2):
	assert len(st1) == len(st2)
	return st1[1::] == st2[0:len(st2)-1]

k = int( sys.stdin.readline().rstrip() ) - 1
text = sys.stdin.readline().rstrip()
patterns = []
for i in range(0, len(text) - k + 1):
	patterns.append( text[i:i+k] )

graph = dict()
	
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