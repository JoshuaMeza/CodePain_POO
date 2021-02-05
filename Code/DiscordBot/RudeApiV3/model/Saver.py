"""
Author CodePain Team
Date 14/01/2021
Version 1.0.1
Saver tool
"""


class Saver:
    def __init__(self, connector):
        """
        This is a constructor
        """
        self.con = connector
        self.words = self.con.getWordsAPI()
        self.custom = {}
        self.requestLog = []
        self.serverSettings = {}
        self.retrieveGuildsInfo()
        self.retrieveCustomWords()

    def getWordsList(self):
        """
        This method returns teh list of banned words
        Args:
            self
            words
        Returns:
            The list of banned words
        """
        return self.words

    def getCustomDict(self):
        """
        This method returns teh list of custom words
        Args:
            self
            words
        Returns:
            The list of custom words
        """
        return self.custom

    def verify(self, userId):
        """
        This method verifies if the user exist in the requests list
        Args:
            self (object): The object itself
            userId (str): User id
            amount (int): Amount of requests
            requestLog (list): List of people that has made requests
        Returns:
            Amount of requests
        """
        amount = 0
        if len(self.requestLog) != 0:
            for user in self.requestLog:
                if str(userId) == user[0]:
                    amount = user[1]
                    break
        return amount

    def addLog(self, userId):
        """
        This method adds a user to the requests list
        Args:
            self (object): The object itself
            userId (str): User id
            requestLog (list): List of people that has made requests
        Returns:
            Nothing
        """
        user = [str(userId), 0]
        self.requestLog.append(user)

    def increaseTimes(self, userId):
        """
        This method increase the number of requests
        Args:
            self (object): The object itself
            userId (str): User id
            requestLog (list): List of people which has made requests
        Returns:
            Nothing
        """
        for user in self.requestLog:
            if str(userId) == user[0]:
                user[1] += 1
                break

    def addRequest(self, userId):
        """
        This method adds a user to the requests list
        Args:
            self (object): The object itself
            userId (str): User id
            requestTimes (int): Number of requests that the user has made
            flag (bool): Verifies if the user can make more requests
        Returns:
            True if the user can make more requests, False if not
        """
        flag = False
        requestTimes = self.verify(userId)

        if requestTimes == 0:
            self.addLog(userId)
            flag = True
        elif requestTimes < 5:
            flag = True

        if flag:
            self.increaseTimes(userId)

        return flag

    def retrieveGuildsInfo(self):
        """
        This method gets the guilds and their modes
        Args:
            self
            serverInfo
            con
            server
            serverData
            serverSettings
        Returns:
            Nothing
        """
        serverInfo = self.con.getGuildsInfo()

        for server in serverInfo:
            serverData = server.split(', ')
            self.serverSettings[serverData[0]] = serverData[1]

    def getSettings(self, guildId):
        """
        This method returns the settings of a server
        Args:
            self
            guildId
            serverSettings
        Returns:
            Penalize mode (1 or 0)
        """
        return int(self.serverSettings[str(guildId)])

    def setSettings(self, guildId, penMode):
        """
        This method sets a new status into the penalize mode
        Args:
            self
            guildId
            penMode
            flag
            con
            serverSettings
        Returns:
            True if success, False if not
        """
        flag = self.con.setPenalizeMode(guildId, penMode)

        if flag:
            self.serverSettings[str(guildId)] = str(penMode)

        return flag

    def retrieveCustomWords(self):
        """
        """
        custom = self.con.getCustomWords()
        guilds = self.con.getGuildsInfo()

        for item in guilds:
            self.custom[item.split(',')[0]] = []

        for word in custom:
            data = word.split(',')
            self.custom[data[0]].append(data[1])
