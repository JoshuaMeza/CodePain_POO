class BotProtocols:

	def __init__(self):
		self.whitelist = []
		self.banlist = []
		self.admin = []
		self.channels = []
		self.commandChannels = []
		self.currentWords =  ["API"]    #   ToDo
		self.penaltyFlag = 5

	def referee(self, member):
		Saction = False
		if self.penaltyFlag != 0:
			if member["Faults"] == self.penaltyFlag:
				Saction = True
		return Saction

	def setPenaltyFlag(self, flag):
		self.penaltyFlag = flag

	def setAdmin(self, member):
		self.admin.append(member)

	def removeAdmin(self, admin):
		self.admin.remove(admin)

	def manageChannels(self, command, target):
		if command == "add":
			self.channels.append(target)
		elif command == "remove":
			self.channels.remove(target)
		else:
			return self.channels

	def checkmessage(self, message):
		currentWord = ""
		saction = False
		for i in message:
			if i != " ":
				currentWord += i
			else:
				if currentWord in self.currentWords: #ToDo
					saction = True
					break
				else:
					currentWord = ""
		return saction
