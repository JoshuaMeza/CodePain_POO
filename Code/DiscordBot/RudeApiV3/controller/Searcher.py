"""
Author CodePain Team
Date 14/01/2021
Version 1.0.0
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

    def searchWord(self, text, guildId):
        """
        This method verifies if a word in the text is already in the list
        Args:
            self (object): The object itself
            text (str): A text
            splittedText (list): Words from the text separated by spaces
            words (list): Banned words
            flag (bool): Verifies if the word was found
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
            self
            word
            guildId
            flag
            custom
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
            self
            word
            guildId
            flag
            ignore
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
            self
            compareOne
            compareTwo
        Returns:
            True if equal or similar, False if not
        """
        return compareOne == compareTwo
