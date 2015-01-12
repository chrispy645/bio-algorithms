import sys
import Queue

def combine(st1,st2):
	assert st1[1::] == st2[0:len(st2)-1]
	return st1 + st2[ len(st2) - 1 ]
	
def can_combine(st1,st2):
	if st1[1::] == st2[0:len(st2)-1]:
		return True
	return False

sys.stdin.readline()
patterns = []
for line in sys.stdin:
	patterns.append( line.rstrip() )

	
def bfs():
	Q = Queue.Queue()
	V = set()
	for pattern in patterns:
		new_patterns = list(patterns)
		new_patterns.remove(pattern)
		node = {'current_kmer': pattern, 'total_string': [pattern], 'patterns_left': new_patterns }
		Q.put(node)
	while not Q.empty():
		t = Q.get()
		if len(t['patterns_left']) == 0:
			return t['total_string']
		for pattern_left in t['patterns_left']:
			if can_combine(t['current_kmer'], pattern_left):
				new_total_string = list(t['total_string'])
				new_total_string.append(pattern_left)
				new_patterns_left = list(t['patterns_left'])
				new_patterns_left.remove(pattern_left)
				node = {'current_kmer': pattern_left, 'total_string': new_total_string, 'patterns_left': new_patterns_left }
				Q.put(node)

				

final = bfs()
st = final[0]
for i in range(1, len(final)):
	st += final[i][ len(final[i])-1 ]
print st