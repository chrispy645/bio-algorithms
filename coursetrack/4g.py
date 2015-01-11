import sys

sys.setrecursionlimit(1000000)

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

finals = []
def find(current_kmer, total_string, patterns_left):
	# base case
	if len(patterns_left) == 0:
		#finals.append(total_string)
		#return
		st = total_string[0]
		for i in range(1, len(total_string)):
			st += total_string[i][ len(total_string[i])-1 ]
		print st
		sys.exit(0)
	# find kmers in patterns_left that will match
	for pattern_left in patterns_left:
		if can_combine(current_kmer, pattern_left):
			new_total_string = list(total_string)
			new_total_string.append(pattern_left)
			new_patterns_left = list(patterns_left)
			new_patterns_left.remove(pattern_left)
			find(pattern_left, new_total_string, new_patterns_left)
		
for pattern in patterns:		
	new_patterns = list(patterns)
	new_patterns.remove(pattern)
	find(pattern, [pattern], new_patterns)

"""
for final in finals:
	st = final[0]
	for i in range(1, len(final)):
		st += final[i][ len(final[i])-1 ]
	print st
"""