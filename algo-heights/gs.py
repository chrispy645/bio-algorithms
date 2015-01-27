import sys

def search(dd, i, seen):
	seen.add(i)
	for child in dd[i]:
		if child not in seen:
			search(dd, child, seen)

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
	succ = False
	for key in dd:
		seen = set()
		search(dd, key, seen)
		#print seen
		if len(seen) == len(dd.keys()):
			print key,
			succ = True
			break
	if not succ:
		print -1,