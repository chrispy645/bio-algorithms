import sys

n = [int(x) for x in sys.stdin.readline().rstrip().split()][0]

dd = dict()
for line in sys.stdin:
	digits = [ int(x) for x in line.rstrip().split() ]
	if digits[0] not in dd:
		dd[digits[0]] = []
	dd[digits[0]].append(digits[1])
	if digits[1] not in dd:
		dd[digits[1]] = []
	dd[digits[1]].append(digits[0])


for i in range(1, n+1):
	if i not in dd:
		print 0,
	else:
		neighbors = dd[i]
		sum = 0
		for neighbor in neighbors:
				sum += len(dd[neighbor])
		print sum,