"""
Longest common subsequence problem
"""

import sys

class Node(object):
    def __init__(self):
        self.value = 0
        self.ptr = None
    def __str__(self):
        return str(self.value)

def printgrid():
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            print grid[i][j],
        print
    print

X = '-' + sys.stdin.readline().rstrip()
Y = '-' + sys.stdin.readline().rstrip()

m = len(X) # num edges making up rows
n = len(Y) # num edges making up cols

# 0...n+1 = [0..n], and 0...m+1 = [0..m]
grid = [ [Node() for j in range(0,n)] for i in range(0,m) ]

#print m,
#print n

#print X
#print Y

#printgrid()

for i in range(1, m):
    for j in range(1, n):
        """
        s[i][j] = max{ s[i-1][j]+0, s[i][j-1]+0, s[i-1][j-1]+1 if v[i]=w[j]
        """

        if X[i] == Y[j]:
            grid[i][j].value = max( grid[i-1][j-1].value+1, grid[i][j-1].value, grid[i-1][j].value )
        else:
            grid[i][j].value = max( grid[i][j-1].value, grid[i-1][j].value )

        if grid[i][j].value == grid[i-1][j].value:
            grid[i][j].ptr = "up"
        elif grid[i][j].value == grid[i][j-1].value:
            grid[i][j].ptr = "left"
        elif grid[i][j].value == (grid[i-1][j-1].value+1):
            grid[i][j].ptr = "diag"



printgrid()

i = m-1
j = n-1

#print i,
#print j

#sys.exit(0)

st = []
while True:
    if i == 0 or j == 0:
        break
    if grid[i][j].ptr == "up":
        i = i-1
    elif grid[i][j].ptr == "left":
        j = j-1
    elif grid[i][j].ptr == "diag":
        st.append( X[i] )
        i = i-1
        j = j-1

print "".join(st)[::-1]
