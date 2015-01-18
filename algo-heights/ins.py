import sys

def swap(arr, i ,j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def insertion_sort(arr):
	swaps = 0
	for i in range(1, len(arr)):
		k = i
		while k > 0 and arr[k] < arr[k-1]:
			swap(arr, k-1, k)
			swaps += 1
			k = k -1
	return swaps
			
sys.stdin.readline()
arr = [int(x) for x in sys.stdin.readline().rstrip().split()]
print insertion_sort(arr)