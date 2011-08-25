from collections import defaultdict

class Element():
	def __init__(self,obj=None):
		self.obj = obj
		self.children = defaultdict(Element)
		
	def get(self,iterable=()):
		if len(iterable) > 0:
			return self.children[iterable[0]].get(iterable[1:])
		else:
			return self
			
	def add(self,obj,iterable=()):
		if len(iterable) > 0:
			self.children[iterable[0]].add(obj,iterable[1:])
		else:
			self.obj = obj
