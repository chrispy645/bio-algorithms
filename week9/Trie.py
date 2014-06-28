class Trie(object):

	def __init__(self, strs = []):
		self.root = dict()
		for str in strs:
			self.insert(str)
		
	def insert(self, str):
		current_node = self.root
		for key in str + '$':
			if key not in current_node:
				current_node[key] = dict() if key != '$' else None
			current_node = current_node[key]
	
	def parse(self, str):
		current_node = self.root
		for key in str:
			if key not in current_node:
				return False
			else:
				current_node = current_node[key]
		return True
			