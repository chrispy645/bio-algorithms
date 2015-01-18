import sys

sys.stdin.readline()
arr1 = [int(x) for x in sys.stdin.readline().rstrip().split()]
sys.stdin.readline()
arr2 = [int(x) for x in sys.stdin.readline().rstrip().split()]

i = 0
j = 0
new_arr = []
while True:
	if i >= len(arr1):
		for j in range(j, len(arr2)):
			new_arr.append(arr2[j])
		break
	if j >= len(arr2):
		for i in range(i, len(arr1)):
			new_arr.append(arr1[i])
		break	
	if arr1[i] < arr2[j]:
		new_arr.append(arr1[i])
		i += 1
	else:
		new_arr.append(arr2[j])
		j += 1
		
for n in new_arr:
	print n,