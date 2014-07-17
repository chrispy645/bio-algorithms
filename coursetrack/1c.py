import sys

pattern = sys.stdin.readline().rstrip()
genome = sys.stdin.readline().rstrip()

idxs = set()

for i in range(0, len(genome)):
    idx = genome[i::].find(pattern)
    if idx == -1:
        break
    idxs.add(idx+i)

for idx in idxs:
    print idx,
