import sys

text = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline().rstrip())

hm=dict()
hm['A'] = [float(x) for x in sys.stdin.readline().rstrip().split()]
hm['C'] = [float(x) for x in sys.stdin.readline().rstrip().split()]
hm['G'] = [float(x) for x in sys.stdin.readline().rstrip().split()]
hm['T'] = [float(x) for x in sys.stdin.readline().rstrip().split()]


mx = -1
best_kmer = None

def get_prod(kmer):
	prod = 1
	for j in range(0, len(kmer)):
		prod = prod * hm[ kmer[j] ][j]
	return prod
		
for i in range(0, len(text) - k + 1):
	kmer = text[i:i+k]
	print kmer,
	prod = get_prod(kmer)
	print prod
	if prod > mx:
		mx = prod
		best_kmer = kmer
		
print best_kmer