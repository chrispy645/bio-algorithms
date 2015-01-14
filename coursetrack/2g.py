import operator
import sys

spectrum = sorted([ int(x) for x in sys.stdin.readline().rstrip().split() ])
if spectrum[0] != 0:
	spectrum = [0] + spectrum

#spectrum = [0,113,114,128,129,227,242,242,257,355,356,370,371]

dd = dict()

for i in range(0, len(spectrum)):
	for j in range(i+1, len(spectrum)):
		diff = abs(spectrum[j] - spectrum[i])
		if diff == 0:
			continue
		if diff not in dd:
			dd[diff] = 1
		else:
			dd[diff] += 1
			
sorted_dd = sorted(dd.items(), key=operator.itemgetter(1), reverse=True)

for elem in sorted_dd:
	for i in range(0, elem[1]):
		print elem[0],