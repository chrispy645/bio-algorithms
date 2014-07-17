import sys

class Node(object):
    def __init__(self):
        self.right = None
        self.down = None
        self.value = 0
        self.ptr = None
    def __str__(self):
        return str(self.value) + '(d=' + str(self.down) + ',r=' + str(self.right) + ')'

s = sys.stdin.readline().rstrip().split()
n = int(s[0]) # num edges making up rows
m = int(s[1]) # num edges making up cols

grid = [ [Node() for y in range(0,m+1)] for x in range(0,n+1) ]

#print n,
#print m

for i in range(0, n):
    s = [ int(x) for x in sys.stdin.readline().rstrip().split() ]
    row = grid[i]
    for j in range(0, len(s)):
        row[j].down = s[j]

assert sys.stdin.readline().rstrip() == '-'

for i in range(0, n+1):
    s = [int(x) for x in sys.stdin.readline().rstrip().split() ]
    row = grid[i]
    for j in range(0, len(s)):
        row[j].right = s[j]

# do the first row and the first column
for i in range(1, len(grid[0])):
    grid[0][i].value = ( grid[0][i-1].value + grid[0][i-1].right )
    #print grid[0][i]
#print
for i in range(1, len(grid)):
    grid[i][0].value = ( grid[i-1][0].value + grid[i-1][0].down )
    #print grid[i][0]

# do the rest
for i in range(1, len(grid)):
    for j in range(1, len(grid[0])):
        """
        s[i][j] = max{ s[i-1][j].val + s[i-1][j].down, s[i][j-1].val + s[i][j-1].right }
        """
        left = grid[i-1][j].value + grid[i-1][j].down
        top = grid[i][j-1].value + grid[i][j-1].right
        grid[i][j].value = left if left > top else top
        grid[i][j].ptr = grid[i-1][j] if left > top else grid[i][j-1]

node = grid[n][m]
print node.value

