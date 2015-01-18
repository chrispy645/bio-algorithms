import sys
from collections import Counter

def greedy_motif_search(dna, k):
	# best motif matrix
	best_motifs = []
	for seq in dna:
		best_motifs.append( seq[0:k] )
	# for each kmer in the first string from dna
	for x in range(0, len(dna[0]) - k + 1):
		kmer = dna[0][x:x+k]
		motifs = [kmer]
		for i in range(1, len(dna)):
			profile = form_profile(motifs)
			motif_i = most_probable(profile, dna[i], k)
			motifs.append(motif_i)
		if score(motifs) < score(best_motifs):
			best_motifs = motifs
	return best_motifs

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
	
#pp = form_profile(["GGC", "AAG"])
#print most_probable(pp, "CAAGGAGTTCGC", 3)

def consensus(motifs):
	cons = []
	for i in range(0, len(motifs[0])):
		cc=Counter()
		for motif in motifs:
			cc[motif[i]] += 1
		cons.append( cc.most_common()[0][0] )
	return cons
		
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

k = [ int(x) for x in sys.stdin.readline().split() ][0]
dna = []
for line in sys.stdin:
	dna.append(line.rstrip())

for elem in greedy_motif_search(dna, k):
	print elem