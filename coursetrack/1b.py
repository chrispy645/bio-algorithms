import sys

comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
print "".join([ comp[x] for x in sys.stdin.readline().rstrip() ])[::-1]
