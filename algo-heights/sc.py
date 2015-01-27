import sys

def search(dd, i, seen, tgt):
	if i == tgt:
		return True
	else:
		seen.add(i)
		for child in dd[i]:
			if child not in seen:
				return search(dd, child, seen, tgt)
	return False

for x in range(0,2):
	sys.stdin.readline()
	
graphs = []
current = []
for line in sys.stdin:
	line = line.rstrip()
	if line != "":
		current.append(line)
	else:
		graphs.append(current)
		current = []
graphs.append(current)

dds = []

for gp in graphs:
	dd = dict()
	for i in range(1, int(gp[0].split()[0])+1):
		dd[i] = []
	for line in gp[1::]:
		line = [int(x) for x in line.split()]
		dd[ line[0] ].append(line[1])
	dds.append(dd)
			
for dd in dds:
	succ = True
	for i in range(1, len(dd.keys())+1):
		for j in range(i+1, len(dd.keys())+1):
			if i == j:
				continue
			if search(dd, i, set(), j) == False and search(dd, j, set(), i) == False:
				succ = False
				break
		if succ == False:
			break
	if succ:
		print 1,
	else:
		print -1,