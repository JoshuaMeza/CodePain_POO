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
				target = self.memberStory[member]
				faults = target["Faults"]
				requested = "Found, {0} has {1} stories in this server".format(member, str(faults))
			else:
				requested = "Error, User: {} not found!".format(member)
		else:
			requested = ""
			for (i, j) in zip(self.memberStory.keys(), self.memberStory.values()):
				requested += "{0} has {1} stories in this server\n".format(i,j)
		return requested

	def manageStories(self, member, command):
		if command == "delete":
			ifIn = self.tool_CheckIfIn(member, self.memberStory, [
				"Stories of {} succesfully cleared.".format(member),
				"{} doesn't have an story yet".format(member)])
			if ifIn[0]:
				del self.memberStory[member]
			requested = ifIn[1]
		else:
			ifIn = self.tool_CheckIfIn(member, self.memberStory, [
				"Stories of {} succesfully undone.".format(member),
				"{} doesn't have an story yet".format(member)])
			if ifIn[0]:
				aux = self.memberStory[member]
				aux["Faults"] -= 1
				self.memberStory[member] = aux
			requested = ifIn[1]
		return requested

	@staticmethod
	def tool_CheckIfIn(what, where, msg):
		if what in where:
			result = [True, msg[0]]
		else:
			result = [False, msg[1]]
		return result

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