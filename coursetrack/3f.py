import sys
from collections import Counter
import random

def form_profile(motifs):
	a = []
	c = []
	g = []
	t = []
	for i in range(0, len(motifs[0])):
		occurs = []
		for motif in motifs:
			occurs.append(motif[i])
		a.append( occurs.count('A')+1 / float(len(occurs)+4) )
		c.append( occurs.count('C')+1 / float(len(occurs)+4) )
		g.append( occurs.count('G')+1 / float(len(occurs)+4) )
		t.append( occurs.count('T')+1 / float(len(occurs)+4) )
	return {'A': a, 'C':c, 'G':g, 'T':t }
	
def get_prod(profile, kmer):
	prod = 1
	for j in range(0, len(kmer)):
		prod = prod * profile[ kmer[j] ][j]
	return prod
	
def most_probable(profile, text, k):
	mx = -1
	best_kmer = None	
	for i in range(0, len(text) - k + 1):
		kmer = text[i:i+k]
		prod = get_prod(profile,kmer)
		if prod > mx:
			mx = prod
			best_kmer = kmer
		
	return best_kmer
		
def hamming(s1, s2):
	assert len(s1) == len(s2)
	c = 0
	for i in range(0, len(s1)):
		if s1[i] != s2[i]:
			c += 1
	return c
	
def score(motifs):
	con_str = consensus(motifs)
	c = 0
	for motif in motifs:
		c += hamming(motif, con_str)
	return c
	
def consensus(motifs):
	cons = []
	for i in range(0, len(motifs[0])):
		cc=Counter()
		for motif in motifs:
			cc[motif[i]] += 1
		cons.append( cc.most_common()[0][0] )
	return cons

def randomised_motif_search(dna, k):
	# randomly select kmers motifs
	motifs = []
	for elem in dna:
		a = random.randint(0, len(elem) - k)
		motifs.append( elem[a:a+k] )
	best_motifs = list(motifs)
	while True:
		profile = form_profile(motifs)
		motifs = []
		for elem in dna:
			motifs.append( most_probable(profile, elem, k) )
		if score(motifs) < score(best_motifs):
			best_motifs = motifs
		else:
			return best_motifs
		
	
k = [ int(x) for x in sys.stdin.readline().split() ][0]
dna = []
for line in sys.stdin:
	dna.append(line.rstrip())


best_results = None
min_score = 1000000
for i in range(0, 1000):
	#random.seed(i)
	results = randomised_motif_search(dna, k)
	if score(results) < min_score:
		min_score = score(results)
		best_results = results
	
for res in best_results:
	print res