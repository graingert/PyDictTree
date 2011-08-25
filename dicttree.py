# Copyright 2011 Thomas Grainger <tagrain@gmail.com>
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#                    Version 2, December 2004 
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net> 
#
# Everyone is permitted to copy and distribute verbatim or modified 
# copies of this license document, and changing it is allowed as long 
# as the name is changed. 
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE 
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION 
#
#  0. You just DO WHAT THE FUCK YOU WANT TO. 

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
			
	def add(self,iterable=(),obj=None):
		if len(iterable) > 0:
			self.children[iterable[0]].add(iterable[1:],obj)
		else:
			self.obj = obj
