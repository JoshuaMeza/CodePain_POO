class Tools:

	@staticmethod
	def ListElements(iteration, msg):
		counter = 0
		string = "{}.\n".format(msg)
		for i in iteration:
			counter += 1
			string += "{0}.- {1}\n".format(str(counter), i)
		return string

	@staticmethod
	def CheckIfIn(what, where, msg):
		isIn = False
		if what in where:
			isIn = True
		if isIn:
			results = msg[0]
		else:
			results = msg[1]
		return results

	#ToDo: Start the reading of database, return data on a list.
	@staticmethod
	def CheckDatabase(where, target = None):
		#if target is None, that means that all content must be shown.
		pass

	#ToDo: Remove and Add from database, return feedback (if done or is not there).
	@staticmethod
	def ModifyDatabase(where, target, action = None):
		isIn = False
		pass