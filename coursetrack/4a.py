import sys
import itertools
import operator

k = int( sys.stdin.readline().rstrip() )
text = sys.stdin.readline().rstrip()

kmers = []
for i in range(0, len(text) - k + 1):
	kmers.append( text[i:i+k] )
	
for elem in sorted(kmers):
	print elem