import sys

def search(dd, i, seen):
	if len(seen) == len(dd.keys()):
		return seen
	for child in dd[i]:
		if child not in seen:
			return search(dd, child, seen + [child])
	return None

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

print len(graphs)
sys.exit(0)

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
		path = search(dd, key, [key])
		if path != None:
			print "1 " + " ".join( [str(x) for x in path] )
			succ = True
			break
	if not succ:
		print "-1"
	