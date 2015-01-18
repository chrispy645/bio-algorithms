import sys
dd=dict()

n = [int(x) for x in sys.stdin.readline().rstrip().split()][0]


for line in sys.stdin:
	digits = [int(x) for x in line.rstrip().split()]
	for digit in digits:
		if digit not in dd:
			dd[digit] = 1
		else:
			dd[digit] += 1

	
for i in range(1,n+1):
	print dd[i],

