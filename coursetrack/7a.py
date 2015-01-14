import sys

class Trie(object):

	def __init__(self, strs = []):
		self.root = (1, dict())
		self.counter = 2
		for str in strs:
			self.insert(str)
		
	def insert(self, str, debug=False):
		current_node = self.root
		for key in str + '$':
			if key not in current_node[1]:
				if key != '$':
					current_node[1][key] = (self.counter, dict())
					if debug:
						print current_node[0],
						print self.counter,
						print key
					self.counter += 1
				else:
					current_node[1][key] = (None, None)
			current_node = current_node[1][key]
	
	# kinda works?
	def parse(self, str):
		current_node = self.root
		for key in str + '$':
			if key not in current_node[1]:
				if '$' in current_node[1]:
					return True
				else:
					return False
			else:
				current_node = current_node[1][key]
				if key == '$':
					return True
		return False
		
words = [x.rstrip() for x in sys.stdin]
tt = Trie()
for word in words:
	tt.insert(word, debug=True)