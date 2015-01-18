import sys

dd=dict()
k = int( sys.stdin.readline().rstrip().split()[0] )
for line in sys.stdin:
	nums = [int(x) for x in line.rstrip().split()]
	if nums[0] not in dd:
		dd[nums[0]] = []
	dd[nums[0]].append(nums[1])
for i in range(1, k+1):
	if i not in dd:
		dd[i] = []
		
def dfs(graph, root):
	seen.add(root)
	for child in graph[root]:
		if child not in seen:
			dfs(graph, child)
	postorder.append(root)
		
seen = set()
postorder = []
for key in dd:
	if key not in seen:
		dfs(dd, key)
		
for elem in postorder[::-1]:
	print elem,