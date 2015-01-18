import sys
import Queue

graph_text = []
sys.stdin.readline()
sys.stdin.readline()
curr = []
for line in sys.stdin:
	line = line.rstrip()
	if line == "":
		graph_text.append(curr)
		curr = []
	else:
		curr.append(line)
graph_text.append(curr)		
		
graphs = []
for gp in graph_text:
	k = int( gp[0].split()[0] )
	dd = dict()
	for line in gp[1::]:
		nums = [int(x) for x in line.split()]
		if nums[0] not in dd:
			dd[nums[0]] = []
		dd[nums[0]].append(nums[1])
	for i in range(1, k+1):
		if i not in dd:
			dd[i] = []
	graphs.append(dd)
	
"""		
def _dfs(graph, root, seen):
	if root in seen:
		return True
	else:
		for child in graph[root]:
			return _dfs( graph, child, set( list(seen) + [root] ) )
	return False

def dfs(graph):
	for node in graph:
		val = _dfs(graph, node, set())
		if val == True:
			return True
	return False
"""

def has_leafs(graph):
	for key in graph:
		children = graph[key]
		if len(children) == 0:
			return True
	return False
	
def return_leaf(graph):
	for key in graph:
		children = graph[key]
		if len(children) == 0:
			return key
	return None
	
for graph in graphs:
	while True:
		# if graph has no nodes, stop - it is acyclic
		if len(graph.keys()) == 0:
			print "1",
			break
		# if the graph has no leaf, stop - it is cyclic
		elif has_leafs(graph) == False:
			print "-1",
			break
		# choose a leaf, remove this leaf and all edges going into this leaf
		else:
			leaf = return_leaf(graph)
			if leaf == None:
				print "-1",
				break
			del graph[leaf]
			for key in graph:
				children = graph[key]
				if leaf in children:
					children.remove(leaf)
	