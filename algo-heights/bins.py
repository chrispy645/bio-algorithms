import sys
import time

sys.stdin.readline()
sys.stdin.readline()

def binary_search(arr, key, mn, mx):
	mid = (mx+mn)/2
	if mx-mn == 1 and arr[mid] != key:
		return -1
	if arr[mid] > key:
		return binary_search(arr, key, mn, mid)
	elif arr[mid] < key:
		return binary_search(arr, key, mid, mx)
	elif arr[mid] == key:
		return mid

		
#arr = [1,2,3,4,5]
#for key in [1,2,3,4,5,10]:
#	print binary_search(arr, key, 0, len(arr))	
#		
#sys.exit(0)		
		
arr = [int(x) for x in sys.stdin.readline().split()]

keys = [int(x) for x in sys.stdin.readline().split()]
for key in keys:
	idx = binary_search(arr, key, 0, len(arr))
	if idx != -1:
		idx += 1
	print idx,