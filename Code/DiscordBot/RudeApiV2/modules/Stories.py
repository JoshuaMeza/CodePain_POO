from RudeApiV2.modules.Tools import Tools

class Stories:
	def __init__(self):
		self.tools = Tools()

	def newStory(self, member):
		memberStory = self.tools.CheckDatabase("stories")
		if member in memberStory:
			aux = memberStory[member]
			aux["Faults"] += 1
			memberStory[member] = aux
		else:
			memberStory[member] = {"Faults" : 1}

		self.tools.ModifyDatabase("stories", memberStory, "replace")

	def getStories(self, member= None):
		if member is not None:
			memberStory = self.tools.CheckDatabase("stories", member)
			if memberStory.get(member) is not None:
				target = memberStory[member]
				faults = target["Faults"]
				requested = ["Found, {0} has {1} stories in this server".format(member, str(faults))]
			else:
				requested = ["Error, User: {} not found!".format(member)]
		else:
			memberStory = self.tools.CheckDatabase("stories")
			requested = []
			for (i, j) in zip(memberStory.keys(), memberStory.values()):
				requested.append("{0} has {1} stories in this server\n".format(i,j))
		return requested

	def manageStories(self, member, command):
		memberStory = self.tools.CheckDatabase("stories", member)
		if command == "del":
			ifIn = self.tool_CheckIfIn(member, memberStory, [
				"Stories of {} succesfully cleared.".format(member),
				"{} doesn't have an story yet".format(member)])
			if ifIn[0]:
				del memberStory[member]
			requested = ifIn[1]
		else:
			ifIn = self.tool_CheckIfIn(member, memberStory, [
				"Stories of {} succesfully undone.".format(member),
				"{} doesn't have an story yet".format(member)])
			if ifIn[0]:
				aux = memberStory[member]
				aux["Faults"] -= 1
				memberStory[member] = aux
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