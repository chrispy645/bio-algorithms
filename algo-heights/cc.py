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
		dd[i] = []
	
seen = set()
def dfs(i):
	seen.add(i)
	for neighbor in dd[i]:
		if neighbor not in seen:
			dfs(neighbor)

ccs = 0
for i in range(1, n+1):
	if i not in seen:
		ccs += 1
		dfs(i)
		
print ccs