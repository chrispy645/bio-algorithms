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
		for key in str + '$':
			if key not in current_node:
				if '$' in current_node:
					return True
				else:
					return False
			else:
				current_node = current_node[key]
				if key == '$':
					return True
		return False
			