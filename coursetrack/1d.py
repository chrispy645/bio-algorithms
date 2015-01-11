import operator
import sys

genome = sys.stdin.readline().rstrip()
nums = sys.stdin.readline().rstrip().split(' ')
k = int(nums[0])
L = int(nums[1])
t = int(nums[2])

ss = set()
for x in range(0, len(genome) - L + 1):
	substr = genome[x:x+L]
	dd = dict()
	for i in range(0, len(substr) - k + 1):
		kmer = substr[i:i+k]
		if kmer not in dd:
			dd[kmer] = 1
		else:
			dd[kmer] += 1
	dd = sorted(dd.items(), key=operator.itemgetter(1), reverse=True)
	for elem in dd:
		if elem[1] >= t:
			ss.add(elem[0])

print " ".join(ss)