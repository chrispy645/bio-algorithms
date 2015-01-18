import sys

"""
Compute the reverse graph!!!
"""
dd=dict()
reverse_dd=dict()
k = int( sys.stdin.readline().rstrip().split()[0] )
for line in sys.stdin:
	nums = [int(x) for x in line.rstrip().split()]	
	if nums[0] not in dd:
		dd[nums[0]] = []
	dd[nums[0]].append(nums[1])	
	if nums[1] not in reverse_dd:
		reverse_dd[nums[1]] = []
	reverse_dd[nums[1]].append(nums[0])
	
for i in range(1, k+1):
	if i not in dd:
		dd[i] = []
	if i not in reverse_dd:
		reverse_dd[i] = []

def compute_postorder(graph):	
	def dfs(graph, root):
		seen.add(root)
		for child in graph[root]:
			if child not in seen:
				dfs(graph, child)
		postorder.append(root)		
	seen = set()
	postorder = []
	for key in graph:
		if key not in seen:
			dfs(graph, key)		
	return postorder[::-1]
	
def connected_components(graph, order):
	def dfs(graph,i, seen):
		seen.add(i)
		for neighbor in graph[i]:
			if neighbor not in seen:
				dfs(graph,neighbor,seen)
	seen = set()
	ccs = 0
	for i in order:
		if i not in seen:
			ccs += 1
			dfs(graph, i, seen)
			
	return ccs
	
order = compute_postorder(reverse_dd)
print connected_components(dd, order)