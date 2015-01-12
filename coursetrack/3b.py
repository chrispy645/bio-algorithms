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
	
def dist(pattern, dna, k):
	distance = 0
	for text in dna:
		hamming_distance = 100000
		for i in range(0, len(text) - k + 1):
			kmer = text[i:i+k]
			if hamming_distance > hamming(kmer, pattern):
				hamming_distance = hamming(kmer, pattern)
		distance = distance + hamming_distance
	return distance


k = int(sys.stdin.readline().rstrip())
dna = []
for line in sys.stdin:
	dna.append(line.rstrip())

kmers = []
for combination in itertools.product(['A','T','C','G'], repeat=k):
	kmers.append( ''.join(map(str,combination)) )	
	
best = "AAA"
min = 10000000
for kmer in kmers:
	val = dist(kmer, dna, k)
	if val < min:
		min = val
		best = kmer
		
print best