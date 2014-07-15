"""
Multiple pattern matching problem
http://rosalind.info/problems/7b/
"""

from SuffixTrie import SuffixTrie

import sys

text = sys.stdin.readline().rstrip()
patterns = [line.rstrip() for line in sys.stdin]

x = SuffixTrie()
x.insert(text)


idxs = []
for pattern in patterns:
	idxs.extend( x.parse(pattern) )
print " ".join( [str(x) for x in sorted(idxs)] )

"""
x=SuffixTrie()
x.insert("ATCG")
print x.parse("A")
"""