import sys
import itertools
import operator

def hamming(st1, st2, d):
	mm = 0
	assert len(st1) == len(st2)
	for x in range(0, len(st1)):
		if st1[x] != st2[x]:
			mm += 1
			# optimisation trick
			if mm > d:
				return 100000
	return mm
	
genome = sys.stdin.readline().rstrip()
nums = sys.stdin.readline().rstrip().split()
k = int(nums[0])
d = int(nums[1])

kmers = []
for combination in itertools.product(['A','T','C','G'], repeat=k):
	kmers.append( ''.join(map(str,combination)) )
	
dd = dict()
for i in range(0, len(genome) - k + 1):
	sys.stderr.write( str(float(i) / float(len(genome)-k-1)) + "\n" )
	substr = genome[i:i+k]
	for kmer in kmers:
		if hamming(kmer, substr, d) <= d:
			if kmer not in dd:
				dd[kmer] = 1
			else:
				dd[kmer] += 1

dd = sorted(dd.items(), key=operator.itemgetter(1), reverse=True)
max_occur = dd[0][1]
for elem in dd:
	if elem[1] != max_occur:
		break
	print elem[0],