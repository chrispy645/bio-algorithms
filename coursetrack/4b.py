import sys
import itertools
import operator

def match(st1,st2):
	assert len(st1) == len(st2)
	return st1[1::] == st2[0:len(st2)-1]

patterns = []
for line in sys.stdin:
	patterns.append( line.rstrip() )

for i in range(0, len(patterns)):
	for j in range(0, len(patterns)):
		if i == j:
			continue
		else:
			if match(patterns[i], patterns[j]):
				print patterns[i] + " -> " + patterns[j]