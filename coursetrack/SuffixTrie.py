"""
Memory hungry since it's a suffix trie, not suffix tree.
"""

class SuffixTrie(object):

	def __init__(self, str=None):
		self.root = [-1, -1, -1, -1, -1]
		self.idr = {'A': 0, 'T': 1, 'C': 2, 'G': 3, '$': 4}
		if str is not None:
			self.insert(str)
		
	def insert(self, str):
		for i in range(0, len(str)):
			suffix = str[i::]
			current_node = self.root
			for key in suffix + '$':
				# if key not in current node:
				# 	current_node[key] = dict() if key != '$' else i
				if current_node[ self.idr[key] ] == -1:
					current_node[ self.idr[key] ] = [-1, -1, -1, -1, -1] if key != '$' else i
				current_node = current_node[ self.idr[key] ]

	"""
	Try and run str down the trie.
	If it is successful, recursively search successor node until
	you obtain an index, than append it to the list, idx.
	"""
	def parse(self, str):
		current_node = self.root
		for key in str:
			if current_node[ self.idr[key] ] == -1:
				return -1
			else:
				current_node = current_node[ self.idr[key] ]
		idxs = []
		self.__exhaust(current_node, idxs)
		return idxs
		
	
	def __count_edge(self, node):
		if isinstance(node,int):
			return []
			
		c = []
		for elem in node:
			if elem != -1:
				c.append(elem)
		return c
	
	"""
	Recursively search nodes in the trie till you find an index.
	If it is not -1, then append it to the list, idxs.
	"""
	def __exhaust(self, node, idxs):
		# first move far down
		while True:
			edges = self.__count_edge(node)
			if len(edges) == 1:
				node = edges[0]
			# it's an index node
			elif len(edges) == 0:
				idxs.append(node)
				break
			elif len(edges) > 1:
				for edge in edges:
					self.__exhaust(edge, idxs)
				break
		