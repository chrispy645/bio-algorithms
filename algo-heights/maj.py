import sys
from collections import Counter

sys.stdin.readline()
for line in sys.stdin:
	arr = [int(x) for x in line.rstrip().split()]
	cc = Counter()
	for elem in arr:
		cc[elem] += 1
	if cc.most_common()[0][1] > len(arr)/2:
		print cc.most_common()[0][0],
	else:
		print -1,