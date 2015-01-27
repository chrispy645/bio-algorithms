import sys

sys.stdin.readline()

arr = [int(x) for x in sys.stdin.readline().rstrip().split()]
repeat = arr.count(arr[0])
i = arr[0]
arr = [x for x in arr if x != i]

for k in [x for x in arr if x <= i]:
    print k,
    
for k in [i for x in range(0, repeat)]:
    print k,
    
for k in [x for x in arr if x > i]:
    print k,
