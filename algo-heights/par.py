import sys

sys.stdin.readline()
arr = [int(x) for x in sys.stdin.readline().rstrip().split()]

for k in [x for x in arr[1::] if x <= arr[0]]:
    print k,
print arr[0],
for k in [x for x in arr[1::] if x > arr[0]]:
    print k,
