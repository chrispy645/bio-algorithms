"""
Frequent words problem
http://rosalind.info/problems/1a/
"""


import sys

text = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline().rstrip())

hm = dict()

for i in range(0, len(text)-k+1):
	seg = text[i:i+k]
	if seg not in hm:
		hm[seg] = 1
	else:
		hm[seg] += 1
		
best = 0
best_kmer = []
for key in hm:
	if hm[key] > best:
		best = hm[key]
		best_kmer = [ key ]
	elif hm[key] == best:
		best_kmer.append(key)
		
print " ".join(best_kmer)