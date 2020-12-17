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
		return self.tool_Iteration(self.admin, "List of current admins")

	def manageChannels(self, command, channelType, target = None):
		requested = True
		if command == "add":
			if channelType == "command_channels":
				self.commandChannels.append(target)
			else:
				self.channels.append(target)
		elif command == "remove":
			if channelType == "command_channels":
				if target in self.commandChannels:
					self.commandChannels.remove(target)
				else:
					requested = target + " is not in the channel list"
			else:
				if target in self.channels:
					self.channels.remove(target)
				else:
					requested = target + " is not in the channel list"
		else:
			if channelType == "command_channels":
				iteration = [self.commandChannels, "List of current command channels"]
			else:
				iteration = [self.channels, "List of current moderation channels"]
			requested = self.tool_Iteration(iteration[0], iteration[1])
		return requested

	def manageLists(self, command, listType, target = None):
		if command == "add":
			if listType == "banlist":
				self.banlist.append(target)
			else:
				self.whitelist.append(target)
			requested = "{0} succesfully added to {1}".format(target, listType)
		elif command == "remove":
			if listType == "banlist":
				where = self.banlist
			else:
				where = self.whitelist
			requested = self.tool_CheckIfIn(target, where, [
				"{0} succesfully delethed from {1}!".format(target, listType),
				"{0} is not in {1}".format(target, listType)])
		else:
			if listType == "banlist":
				where = self.banlist
			else:
				where = self.whitelist
			requested = self.tool_Iteration(where, listType)
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

	@staticmethod
	def tool_Iteration(iteration, msg):
		counter = 0
		string = "{}.\n".format(msg)
		for i in iteration:
			counter += 1
			string += "{0}.- {1}\n".format(str(counter), i)
		return string

	@staticmethod
	def tool_CheckIfIn(what, where, msg):
		isIn = False
		if what in where:
			isIn = True
		if isIn:
			results = msg[0]
		else:
			results = msg[1]
		return results