class SuffixTrie(object):

	def __init__(self, str=None):
		self.root = dict()
		if str is not None:
			self.insert(str)
		
	def insert(self, str):
		for i in range(0, len(str)):
			suffix = str[i::]
			current_node = self.root
			for key in suffix + '$':
				if key not in current_node:
					current_node[key] = dict() if key != '$' else i
				current_node = current_node[key]

	"""
	Try and run str down the trie.
	If it is successful, recursively search successor node until
	you obtain an index, than append it to the list, idx.
	"""
	def parse(self, str):
		current_node = self.root
		for key in str:
			if key not in current_node:
				return -1
			else:
				current_node = current_node[key]
		idxs = []
		self.__exhaust(current_node, idxs)
		return idxs
		
	"""
	Recursively search nodes in the trie till you find an index.
	If it is not -1, then append it to the list, idxs.
	"""
	def __exhaust(self, node, idxs):
		if isinstance(node, int):
			if node != -1:
				idxs.append(node)
		else:
			for key in node:
				self.__exhaust(node[key], idxs)
		