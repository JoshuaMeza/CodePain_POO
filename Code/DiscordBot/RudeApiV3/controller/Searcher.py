"""
Author CodePain Team
Date 14/01/2021
Version 1.0.1
Searcher tool
"""


class Searcher:
    def __init__(self, memory):
        """
        This is a constructor
        """
        self.words = memory.getWordsList()
        self.custom = memory.getCustomDict()
        self.ignore = memory.getIgnoredDict()
        self.whitelist = memory.getWhiteList()

    def searchWord(self, text, guildId):
        """
        This method verifies if a word in the text is already in the list
        Args:
            self (object): The object itself
            text (str): A text
            splittedText (list): Words from the text separated by spaces
            words (list): Banned words
            flag (bool): Verifies if the word was found
            word (str): Word in text
            newWord (str): Word in upper case
            swering (str): Word in banned words list
        Returns:
            True if that word exist in the list, False if not
        """
        splittedText = text.split(' ')
        flag = False

        for word in splittedText:
            newWord = word.upper()
            if self.words is not None:
                for swering in self.words:
                    if self.searchIgnore(newWord, guildId):
                        continue
                    elif self.searchAlgorithm(newWord, swering) or self.searchCustom(newWord, guildId):
                        flag = True
                        break
                if flag:
                    break

        return flag

    def searchCustom(self, word, guildId):
        """
        This method searches for custom words
        Args:
            self (object): The object itself
            word (str): Word to verify
            guildId (int): Guild ID
            flag (bool): Success flag
            custom (dict): Custom words dictionary
            item (str): Word in the custom list
        Returns:
            True if that word exist in the list, False if not
        """
        flag = False

        for item in self.custom[str(guildId)]:
            if self.searchAlgorithm(word, item):
                flag = True
                break

        return flag

    def searchIgnore(self, word, guildId):
        """
        This method searches for ignored words
        Args:
            self (object): The object itself
            word (str): Word to verify
            guildId (int): Guild ID
            flag (bool): Success flag
            ignore (dict): Ignore words dictionary
            item (str): Word in the ignored list
        Returns:
            True if that word exist in the list, False if not
        """
        flag = False

        for item in self.ignore[str(guildId)]:
            if self.searchAlgorithm(word, item):
                flag = True
                break

        return flag

    def searchAlgorithm(self, compareOne, compareTwo):
        """
        This method does the search
        Args:
            self (object): The object itself
            compareOne (str): Word one
            compareTwo (str): Word two
        Returns:
            True if equal or similar, False if not
        """
        return compareOne == compareTwo

    def verifyUser(self,  userId, guildId):
        """
        This method verifies if a user is on the whitelist
        Args:
            self (object): The object itself
            userId: (int): User ID
            user (str): User ID in whitelist
            whitelist (dict): Whitelist dictionary
        Returns:
            True if they is on it, False if not
        """
        flag = False

        for user in self.whitelist[str(guildId)]:
            if str(userId) == user:
                flag = True
                break

        return flag
