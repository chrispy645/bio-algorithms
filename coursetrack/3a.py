import sys
import itertools
import operator

def hamming(st1, st2):
	mm = 0
	assert len(st1) == len(st2)
	for x in range(0, len(st1)):
		if st1[x] != st2[x]:
			mm += 1
	return mm

nums = sys.stdin.readline().rstrip().split()
k = int(nums[0])
d = int(nums[1])
dna = []
for line in sys.stdin:
	dna.append(line.rstrip())

kmers = []
for combination in itertools.product(['A','T','C','G'], repeat=k):
	kmers.append( ''.join(map(str,combination)) )

kmer_arr = []
for st in dna:
	se = set()
	for i in range(0, len(st) - k + 1):
		ss = st[i:i+k]	
		for elem in kmers:
			if hamming(elem, ss) <= d:
				se.add(elem)
	kmer_arr.append(se)
	
intersect = kmer_arr[0]
for se in kmer_arr[1::]:
	intersect = intersect.intersection(se)

for its in intersect:
	print its,