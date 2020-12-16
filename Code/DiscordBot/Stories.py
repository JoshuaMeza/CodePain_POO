class Stories:
	def __init__(self):
		self.memberStory = {"validator" : {"Faults":0}}

	def newStory(self, member):
		if member in self.memberStory:
			aux = self.memberStory[member]
			aux["Faults"] += 1
			self.memberStory[member] = aux
		else:
			self.memberStory[member] = {"Faults" : 1}


	def getStories(self, member= None):
		if member is not None:
			if self.memberStory.get(member) is not None:
				user = self.memberStory[member]
			else:
				user = {"Error" : "User: {} not found!".format(member)}
		else:
			user = self.memberStory
		return user

	def manageStories(self, member, command):
		if command == "delete":
			del self.memberStory[member]
		elif command == "undo":
			aux = self.memberStory[member]
			aux["Faults"] -= 1
			self.memberStory[member] = aux
		else:
			pass

if __name__ == '__main__':
	h = Stories()
	h.newStory("fabrizio")
	h.newStory("fabrizio")
	print(h.getStories())
	h.manageStories("fabrizio", "undo")
	print(h.getStories("fabrizio"))
	h.manageStories("fabrizio", "penalty")
	print(h.getStories("fabrizio"))
	h.manageStories("fabrizio", "delete")
	print(h.getStories("fabrizio"))