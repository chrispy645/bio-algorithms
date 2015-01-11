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

pep = sys.stdin.readline().rstrip()
peptide = pep + pep

arr = [0]
for k in range(1,len(pep)):
	for x in range( len(pep), len(peptide) ):
		#print peptide[x-k:x][::-1]
		arr.append( mass( peptide[x-k:x][::-1] ) )
arr.append( mass(pep) )

for elem in sorted(arr):
	print elem,