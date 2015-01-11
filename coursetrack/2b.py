import sys

table = {
'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 
'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y', 
'TGT': 'C', 'TGC': 'C', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 
'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 
'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 
'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I', 
'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 
'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 
'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 
'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 
'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 
'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 
'GGG': 'G', 'TAA': 'X', 'TAG': 'X', 'TGA': 'X' }

pattern = sys.stdin.readline().rstrip()
peptide = sys.stdin.readline().rstrip()

def rc(st):
	st = st[::-1]
	st = list(st)
	for x in range(0, len(st)):
		if st[x] == 'A':
			st[x] = 'T'
		elif st[x] == 'T':
			st[x] = 'A'
		elif st[x] == 'C':
			st[x] = 'G'
		elif st[x] == 'G':
			st[x] = 'C'
	return "".join(st)

k = len(peptide)*3

for x in range(0, len(pattern) - k + 1):
	substr = pattern[x:x+k]
	translated = ""
	for i in range(0, len(substr), 3):
		translated += table[ substr[i:i+3] ]
	if translated == peptide:
		print substr
		
#rc
pattern = rc(pattern)
for x in range(0, len(pattern) - k + 1):
	substr = pattern[x:x+k]
	translated = ""
	for i in range(0, len(substr), 3):
		translated += table[ substr[i:i+3] ]
	if translated == peptide:
		print rc(substr)		
		