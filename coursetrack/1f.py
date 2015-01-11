import sys

def mismatch(st1, st2):
	mm = 0
	assert len(st1) == len(st2)
	for x in range(0, len(st1)):
		if st1[x] != st2[x]:
			mm += 1
	return mm

pattern = sys.stdin.readline().rstrip()
genome = sys.stdin.readline().rstrip()
d = int(sys.stdin.readline().rstrip())

k = len(pattern)
for x in range(0, len(genome) - k + 1):
	substr = genome[x:x+k]
	if mismatch(pattern,substr) <= d:
		print x,