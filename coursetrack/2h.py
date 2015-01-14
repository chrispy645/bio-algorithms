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
	if len(st) == 0:
		return 0
	sum = 0
	for elem in st:
		sum += elem
	return sum
	
def get_spectra(pep):
	peptide = pep + pep
	arr = [0]
	for k in range(1,len(pep)):
		for x in range( len(pep), len(peptide) ):
			arr.append( mass( peptide[x-k:x][::-1] ) )
	arr.append( mass(pep) )
	return sorted(arr)
	
def score(peptide, spectra):
	orig_len = len(spectra)
	peptide_spectra = get_spectra(peptide)
	spec = list(spectra)
	for elem in peptide_spectra:
		if elem in spec:
			spec.remove(elem)
	return orig_len - len(spec)
	
def ldr_best_n(ldr, n):
	if n >= len(ldr):
		return ldr
	sorted_leaderboard = sorted(ldr, reverse=True, key=lambda tup: tup[1])
	i = sorted_leaderboard[n-1][1]	
	for k in range(0, len(sorted_leaderboard)):
		if sorted_leaderboard[k][1] < i:
			return sorted_leaderboard[0:k]
	return sorted_leaderboard
	
def best_m_alphabet(spectrum, m):
	dd = dict()
	for i in range(0, len(spectrum)):
		for j in range(i+1, len(spectrum)):
			diff = abs(spectrum[j] - spectrum[i])
			if diff == 0:
				continue
			if diff < 57 or diff > 200:
				continue
			if diff not in dd:
				dd[diff] = 1
			else:
				dd[diff] += 1
	sorted_dd = sorted(dd.items(), key=operator.itemgetter(1), reverse=True)
	print "full alphabet=" + str(sorted_dd)
	i = sorted_dd[m-1][1]
	for k in range(0, len(sorted_dd)):
		if sorted_dd[k][1] < i:
			return [ tp[0] for tp in sorted_dd[0:k] ]
	return [ tp[0] for tp in sorted_dd ]

def leaderboard(spectrum, N, alphabet):
	leaderboard = [ ([], 0) ]
	leader_peptide = []
	while len(leaderboard) != 0:
		backup = list(leaderboard)
		# leaderboard <- expand(leaderboard)
		new_candidates = []
		for peptide in leaderboard:
			for amino_acid in alphabet:
				new_candidates.append( ( peptide[0]+[amino_acid], score(peptide[0]+[amino_acid], spectrum) ) )
		for new_candidate in new_candidates:
			leaderboard.append(new_candidate)
		# for each peptide in leaderboard...
		to_remove = []
		for peptide in leaderboard:
			if mass(peptide[0]) == spectrum[-1]:
				if score(peptide[0], spectrum) > score(leader_peptide, spectrum):
					leader_peptide = peptide[0]
			elif mass(peptide[0]) > spectrum[-1]:
				to_remove.append(peptide)
		for elem in to_remove:
			leaderboard.remove(elem)
		if backup == leaderboard:
			break
		print leaderboard
		# cut from leaderboard
		leaderboard = ldr_best_n(leaderboard, N)	
		#print leaderboard
	return leader_peptide
	
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
spectrum = [int(x) for x in sys.stdin.readline().split()]
alphabet = best_m_alphabet(spectrum, M)

print "alphabet = " + str(alphabet)
print
solution = leaderboard(spectrum, N, alphabet)

print "-".join( [str(x) for x in solution] )