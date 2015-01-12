import sys
import itertools
import operator

mass_table = \
{
	"G":57,
	"A":71,
	"S":87,
	"P":97,
	"V":99,
	"T":101,
	"C":103,
	"I":113,
	"L":113,
	"N":114,
	"D":115,
	"K":128,
	"Q":128,
	"E":129,
	"M":131,
	"H":137,
	"F":147,
	"R":156,
	"Y":163,
	"W":186
}

def mass(st):
	sum = 0
	for elem in st:
		sum += mass_table[elem]
	return sum
	
def get_spectra(pep):
	peptide = pep + pep
	arr = [0]
	for k in range(1,len(pep)):
		for x in range( len(pep), len(peptide) ):
			arr.append( mass( peptide[x-k:x][::-1] ) )
	arr.append( mass(pep) )
	return sorted(arr)
	
def _get_cycles(st):
	cycles = []
	str = st + st
	for x in range(0, len(st)):
		cycles.append(str[x:x+len(st)])
	return cycles
	
def get_cycles(st):
	return _get_cycles(st) + _get_cycles(st[::-1])

spectrum = [ int(x) for x in sys.stdin.readline().rstrip().split() ]
matching_peptides = set()

candidates = set( mass_table.keys() )
while len(candidates) != 0:
	# trim inconsistent peptides
	to_remove = set()
	for candidate in candidates:
		if mass(candidate) not in spectrum:
			to_remove.add(candidate)
	for elem in to_remove:
		candidates.remove(elem)
	# return any peptides whose theoretical spectra match spectrum	
	for candidate in candidates:
		if get_spectra(candidate) == spectrum:
			matching_peptides.add(candidate)
	# extend each peptide by each of 18 different amino acid masses
	new_candidates = set()
	for candidate in candidates:
		for amino_acid in mass_table.keys():
			new_candidates.add( candidate + amino_acid )
	candidates = new_candidates
	#print candidates

# ok, we have a list of final peptides but we got to get rid of ones
# that are dupes of others (in the cyclic sense... e.g. "KYT" == "YTK")

codes = set()
for matching_peptide in matching_peptides:
	cycles = get_cycles(matching_peptide)
	for cycle in cycles:
		codes.add( "-".join([ str(mass(x)) for x in cycle ]) )

for code in codes:
	print code,
