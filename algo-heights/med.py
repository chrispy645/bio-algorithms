import sys

sys.stdin.readline()
arr = [int(x) for x in sys.stdin.readline().rstrip().split()]
target = int(sys.stdin.readline().rstrip())

print sorted(arr)[target-1]
