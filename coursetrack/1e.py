import sys

arr = [0]
genome = sys.stdin.readline().rstrip()
c = 0
g = 0
for i in range(0, len(genome)):
	if genome[i] == 'C':
		c += 1
	elif genome[i] == 'G':
		g += 1
	arr.append(g-c)
	
min = 0
idxs = []
for i,elem in enumerate(arr):
	if elem < min:
		idxs = [i]
		min = elem
	elif elem == min:
		idxs.append(i)
		
for elem in idxs:
	print elem,