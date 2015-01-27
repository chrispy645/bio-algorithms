import sys

sz = int(sys.stdin.readline())
nums = [int(x) for x in sys.stdin.readline().split()]

def swap(n1, n2):
	assert n1 != 0
	assert n2 != 0
	temp = heap[n1]
	heap[n1] = heap[n2]
	heap[n2] = temp

def insert(num):
	heap[0] += 1
	heap[ heap[0] ] = num
	idx = heap[0]
	while heap[idx] > heap[ idx/2 ] and idx != 0 and idx/2 != 0:
		swap( idx, idx/2 )
		idx = idx/2

heap = [None for x in range(0, sz+1)]
heap[0] = 0
for num in nums:
	insert(num)
	#print heap[0]
	
for h in heap[1::]:
	print h,