import sys
import re

text = sys.stdin.readline().rstrip()
patterns = []
for line in sys.stdin:
	patterns.append(line.rstrip())

all = []	
for pattern in patterns:
	elems = [m.start() for m in re.finditer(pattern, text)]
	for elem in elems:
		all.append(elem)
		
for al in sorted(all):
	print al,