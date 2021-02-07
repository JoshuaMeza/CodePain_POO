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
        self.ignored = {}
        self.requestLog = []
        self.serverSettings = {}
        self.whitelist = {}
        self.retrieveGuildsInfo()
        self.retrieveCustomWords()
        self.retrieveIgnoredWords()
        self.retrieveWhitelist()

    def getWordsList(self):
        """
        This method returns the list of banned words
        Args:
            self
            words
        Returns:
            The banned words list
        """
        return self.words

    def getCustomDict(self):
        """
        This method returns the list of custom words
        Args:
            self
            custom
        Returns:
            The custom words list
        """
        return self.custom

    def getIgnoredDict(self):
        """
        This method returns the list of ignored words
        Args:
            self
            ignored
        Returns:
            The ignored words list
        """
        return self.ignored

    def getWhiteList(self):
        """
        This method returns the whitelist
        Args:
            self
            whitelist
        Returns:
            The whitelist
        """
        return self.whitelist

    def verifyLog(self, userId):
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
        requestTimes = self.verifyLog(userId)

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
        This method gets from the database the custom words
        Args:
            self
            custom
            con
            guilds
            item
            word
            data
        Returns:
            Nothing
        """
        custom = self.con.getCustomWords()
        guilds = self.con.getGuildsInfo()

        for item in guilds:
            self.custom[item.split(',')[0]] = []

        for word in custom:
            data = word.split(',')
            self.custom[data[0]].append(data[1])

    def customAmount(self, guildId):
        """
        This method returns the number of custom words that a server has
        Args:
            self
            guildId
            custom
        Returns:
            The amount of custom words
        """
        return len(self.custom[str(guildId)])

    def addCustom(self, word, guildId):
        """
        This method adds a new custom word
        Args:
            self
            word
            guildId
            flag
            con
            custom
        Returns:
            True if success, False if not
        """
        flag = self.con.addCustomWord(word, guildId)

        if flag:
            self.custom[str(guildId)].append(word)

        return flag

    def delCustom(self, word, guildId):
        """
        This method removes a custom word
        Args:
            self
            word
            guildId
            flag
            item
            con
            custom
        Returns:
            True if success, False if not
        """
        flag = False

        for item in self.custom[str(guildId)]:
            if word == item:
                flag = True
                break

        if flag:
            if self.con.removeCustomWord(word, guildId):
                self.custom[str(guildId)].remove(word)

        return flag

    def retrieveIgnoredWords(self):
        """
        This method gets from the database the ignored words
        Args:
            self
            custom
            con
            guilds
            item
            word
            data
        Returns:
            Nothing
        """
        ignored = self.con.getIgnoredWords()
        guilds = self.con.getGuildsInfo()

        for item in guilds:
            self.ignored[item.split(',')[0]] = []

        for word in ignored:
            data = word.split(',')
            self.ignored[data[0]].append(data[1])

    def ignoredAmount(self, guildId):
        """
        This method returns the number of ignored words that a server has
        Args:
            self
            guildId
            ignored
        Returns:
            The amount of custom words
        """
        return len(self.ignored[str(guildId)])

    def addIgnored(self, word, guildId):
        """
        This method adds a new ignored word
        Args:
            self
            word
            guildId
            flag
            con
            ignored
        Returns:
            True if success, False if not
        """
        flag = self.con.addIgnoredWord(word, guildId)

        if flag:
            self.ignored[str(guildId)].append(word)

        return flag

    def delIgnored(self, word, guildId):
        """
        This method removes an ignored word
        Args:
            self
            word
            guildId
            flag
            item
            con
            ignored
        Returns:
            True if success, False if not
        """
        flag = False

        for item in self.ignored[str(guildId)]:
            if word == item:
                flag = True
                break

        if flag:
            if self.con.removeIgnoredWord(word, guildId):
                self.ignored[str(guildId)].remove(word)

        return flag

    def retrieveWhitelist(self):
        """
        This method gets from the database the whitelist
        Args:
            self
            members
            con
            guilds
            item
            word
            data
        Returns:
            Nothing
        """
        members = self.con.getWhiteList()
        guilds = self.con.getGuildsInfo()

        for item in guilds:
            self.whitelist[item.split(',')[0]] = []

        for member in members:
            data = member.split(',')
            self.whitelist[data[0]].append(data[1])

    def addWhitelist(self, user, guildId):
        """
        This method adds a new member to a whitelist
        Args:
            self
            user
            guildId
            flag
            con
            whitelist
        Returns:
            True if success, False if not
        """
        flag = self.con.addUserToWhitelist(user, guildId)

        if flag:
            self.whitelist[str(guildId)].append(user)

        return flag

    def delWhitelist(self, user, guildId):
        """
        This method removes a member from a whitelist
        Args:
            self
            user
            guildId
            flag
            item
            con
            whitelist
        Returns:
            True if success, False if not
        """
        flag = False

        for item in self.whitelist[str(guildId)]:
            if str(user) == item:
                flag = True
                break

        if flag:
            if self.con.removeUserOfWhitelist(user, guildId):
                self.whitelist[str(guildId)].remove(user)

        return flag

    def whitelistAmount(self, guildId):
        """
        This method returns the number of members in a whitelist
        Args:
            self
            guildId
            whitelist
        Returns:
            The amount of custom words
        """
        return len(self.whitelist[str(guildId)])
