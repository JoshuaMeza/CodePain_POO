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

	def currentPenaltyFlag(self):
		return self.penaltyFlag

	def setAdmin(self, member):
		self.admin.append(member)

	def removeAdmin(self, admin):
		result = False
		if admin in self.admin:
			self.admin.remove(admin)
			result = True
		return result

	def showAdmins(self):
		return self.admin

	def manageChannels(self, command, channelType, target = None):
		if command == "add":
			if channelType == "command_channels":
				self.commandChannels.append(target)
			else:
				self.channels.append(target)
		elif command == "remove":
			if channelType == "command_channels":
				self.commandChannels.remove(target)
			else:
				self.channels.remove(target)
		else:
			if channelType == "command_channels":
				requested = self.commandChannels
			else:
				requested = self.channels
			return requested

	def manageLists(self, command, listType, target = None):
		if command == "add":
			if listType == "banlist":
				self.banlist.append(target)
			else:
				self.whitelist.append(target)
		elif command == "remove":
			if listType == "banlist":
				self.banlist.remove(target)
			else:
				self.whitelist.remove(target)
		else:
			if listType == "banlist":
				requested = self.banlist
			else:
				requested = self.whitelist
			return requested

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

	def validateCmChannel(self, ctx):
		isIn = False
		commands_channels = self.commandChannels
		if str(ctx.channel) in commands_channels or len(commands_channels) == 0:
			isIn = True
		return isIn

	def validateAdmin(self, author):
		isIn = False
		if author in self.admin or len(self.admin) ==0:
			isIn = True
		return isIn