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
            self (object): The object itself
            words (list): Banned words list
        Returns:
            The banned words list
        """
        return self.words

    def getCustomDict(self):
        """
        This method returns the list of custom words
        Args:
            self (object): The object itself
            custom (dict): Custom words dictionary
        Returns:
            The custom words list
        """
        return self.custom

    def getIgnoredDict(self):
        """
        This method returns the list of ignored words
        Args:
            self (object): The object itself
            ignored (dict): Ignored words dictionary
        Returns:
            The ignored words list
        """
        return self.ignored

    def getWhiteList(self):
        """
        This method returns the whitelist
        Args:
            self (object): The object itself
            whitelist (dict): Whitelist dictionary
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
            user (list): User who has requested
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
            user (list): User who has requested
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
            user (list): User who has requested
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
            self (object): The object itself
            serverInfo (list): Servers list 
            con (object): Connector object
            server (str): A server
            serverData (list): Information of a server
            serverSettings (dict): Dictionary of servers and their settings
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
            self (object): The object itself
            guildId (int): Guild ID
            serverSettings (dict): Dictionary of servers and their settings
        Returns:
            Penalize mode (1 or 0)
        """
        return int(self.serverSettings[str(guildId)])

    def setSettings(self, guildId, penMode):
        """
        This method sets a new status into the penalize mode
        Args:
            self (object): The object itself
            guildId (int): Guild ID
            penMode (int): 1 for ON and 0 for OFF
            flag (bool): Result
            con (object): Connector object
            serverSettings (dict): Dictionary of servers and their settings
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
            self (object): The object itself
            words (list): Custom words
            con (object): Connector object
            guilds (list): Servers list 
            item (str): Server info
            word (str): String with Guild ID and Word
            data (list): Word information separated
            custom (dict): Custom words dictionary
        Returns:
            Nothing
        """
        words = self.con.getCustomWords()
        guilds = self.con.getGuildsInfo()

        for item in guilds:
            self.custom[item.split(',')[0]] = []

        for word in words:
            data = word.split(',')
            self.custom[data[0]].append(data[1])

    def customAmount(self, guildId):
        """
        This method returns the number of custom words that a server has
        Args:
            self (object): The object itself
            guildId (int): Guild ID
            custom (dict): Custom words dictionary
        Returns:
            The amount of custom words
        """
        return len(self.custom[str(guildId)])

    def addCustom(self, word, guildId):
        """
        This method adds a new custom word
        Args:
            self (object): The object itself
            word (str): A word
            guildId (int): Guild ID
            flag (bool): Result
            con (object): Connector object
            custom (dict): Custom words dictionary
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
            self (object): The object itself
            word (str): A word
            guildId (int): Guild ID
            flag (bool): Result
            item (str): Guild ID
            con (object): Connector object
            custom (dict): Custom words dictionary
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
            self (object): The object itself
            words (list): Ingnored words
            con (object): Connector object
            guilds (list): Servers list 
            item (str): Server info
            word (str): String with Guild ID and Word
            data (list): Word information separated
            ignored (dict): Ignored words dictionary
        Returns:
            Nothing
        """
        words = self.con.getIgnoredWords()
        guilds = self.con.getGuildsInfo()

        for item in guilds:
            self.ignored[item.split(',')[0]] = []

        for word in words:
            data = word.split(',')
            self.ignored[data[0]].append(data[1])

    def ignoredAmount(self, guildId):
        """
        This method returns the number of ignored words that a server has
        Args:
            self (object): The object itself
            guildId (int): Guild ID
            ignored (dict): Ignored words dictionary
        Returns:
            The amount of custom words
        """
        return len(self.ignored[str(guildId)])

    def addIgnored(self, word, guildId):
        """
        This method adds a new ignored word
        Args:
            self (object): The object itself
            word (str): A word
            guildId (int): Guild ID
            flag (bool): Result
            con (object): Connector object
            ignored (dict): Ignored words dictionary
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
            self (object): The object itself
            word (str): A word
            guildId (int): Guild ID
            flag (bool): Result
            item (str): Guild ID
            con (object): Connector object
            ignored (dict): Ignored words dictionary
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
            self (object): The object itself
            members (list): Whitelist
            con (object): Connector object
            guilds (list): Servers list 
            item (str): Server info
            word (str): String with Guild ID and Word
            data (list): Word information separated
            whitelist (dict): Whitelist dictionary
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
            self (object): The object itself
            user (int): User ID
            guildId (int): Guild ID
            flag (bool): Result
            con (object): Connector object
            whitelist (dict): Whitelist dictionary
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
            self (object): The object itself
            user (int): User ID
            guildId (int): Guild ID
            flag (bool): Result
            item (str): Guild ID
            con (object): Connector object
            whitelist (dict): Whitelist dictionary
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
            self (object): The object itself
            guildId (int): Guild ID
            whitelist (dict): Whitelist dictionary
        Returns:
            The amount of custom words
        """
        return len(self.whitelist[str(guildId)])
