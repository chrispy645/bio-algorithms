import sys
import random
import copy

dd = dict()
for line in sys.stdin:
	line = line.rstrip().split("->")
	frm = int(line[0])
	tgts = [int(x) for x in line[1].split(',')]
	for tgt in tgts:
		if tgt not in dd:
			dd[tgt] = []
	dd[frm] = tgts

def random_walk(graph, starting_node=None):
	if starting_node == None:
		starting_node = random.randint(0, len(dd.keys()) - 1)
	path = [starting_node]
	current_node = starting_node
	while True:
		if len(path) > 1 and current_node == path[0]:
			break
		# what paths can we take?
		paths_to_take = graph[current_node]
		#print paths_to_take
		# choose a node
		chosen_node = paths_to_take[ random.randint(0, len(paths_to_take)-1) ]
		path.append(chosen_node)
		# remove the path from dict
		graph[current_node].remove(chosen_node)
		current_node = chosen_node
	return path
	
def merge(path1, path2, vi):
	pp1 = path1[0:path1.index(vi)]
	pp2 = path1[(path1.index(vi)+1)::]
	return pp1 + path2 + pp2
	
def is_eulerian_cycle(path, graph):
	graph_copy = copy.deepcopy(graph)
	for i in range(0, len(path)-1):
		frm = path[i]
		to = path[i+1]
		graph_copy[frm].remove(to)
	for key in graph_copy:
		if len(graph_copy[key]) > 0:
			return False
	return True

def get_degrees(graph):
	results = []
	for key1 in graph:
		out_deg = len(graph[key1])
		in_deg = 0
		for key2 in graph:
			if key1 in graph[key2]:
				in_deg += 1
		results.append( [key1, in_deg, out_deg] )
	return results

#print is_eulerian_cycle([6,8,7,9,6,5,4,2,1,0,3,2,6], dd)


unbalanced_nodes = []
exit_node = None
for res in get_degrees(dd):
	# if unbalanced
	if res[1] != res[2]:
		unbalanced_nodes.append(res)
assert len(unbalanced_nodes) == 2
# if unbalanced_node[0] has no outgoing edges OR
# unbalanced_node[1] has no in-going edges, then
# unbalanced_node[0] is the exit (and therefore ub[1] is the entry)
if unbalanced_nodes[0][2] == 0 or unbalanced_nodes[1][1] == 0:
	dd[ unbalanced_nodes[0][0] ].append( unbalanced_nodes[1][0] )
	exit_node = unbalanced_nodes[0][0]
else:
	dd[ unbalanced_nodes[1][0] ].append( unbalanced_nodes[0][0] )
	exit_node = unbalanced_nodes[1][0]

#print unbalanced_nodes
#print exit_node

random.seed(3)

copy_dd = copy.deepcopy(dd)

# identify a circuit in G and call it R1
R_i = random_walk(copy_dd)
#print R_i

while True:
	# if R_i contains all edges of G, then stop
	if is_eulerian_cycle(R_i, dd):
		#print "->".join( [str(x) for x in R_i] )
		#print R_i
		trail = R_i[ R_i.index(exit_node) + 1 :: ] + R_i[ 1:R_i.index(exit_node) ] + [exit_node]
		print "->".join( [str(x) for x in trail] )
		sys.exit(0)
	else:
		# if R_i does not contain all edges of G, then let v_i be a node on R_i
		# that is incident with an unmarked edge, e_i
		vi = None
		for node in R_i:
			if len(copy_dd[node]) > 0:
				vi = node
				#print vi
				break
		# build a circuit, Q_i, starting at node v_i and using edge e_i.
		# mark the edges of Q_i
		Q_i = random_walk(copy_dd, starting_node=vi)
		#print Q_i
		# create a new circuit, R_i+1 by patching the circuit Q_i into R_i
		# at v_i.
		R_i = merge(R_i, Q_i, vi)
