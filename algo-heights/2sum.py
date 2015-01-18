import sys

sys.stdin.readline()
arrs = []
for line in sys.stdin:
	arrs.append( [int(x) for x in line.rstrip().split()] )

for arr in arrs:
	success = False
	dd=dict()
	for i,elem in enumerate(arr):
		if elem not in dd:
			dd[elem] = i
		if -elem in dd and dd[elem] != dd[-elem]:
			for x in sorted( [dd[elem]+1, dd[-elem]+1] ):
				print x,
			print
			success = True
			break
	if success == False:
		print -1