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

    def searchWord(self, text):
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
                    # if swering == ignored word -> continue
                    if newWord == swering:
                        flag = True
                        break
                if flag:
                    break

        return flag

    def searchCustom(self, text, guildId):
        """
        This method searches into the custom words
        Args:
            self
            text
            guildId
        Returns
            True if that word exist in the list, False if not
        """
        customList = self.custom[str(guildId)]
        splittedText = text.split(' ')
        flag = False

        for word in splittedText:
            newWord = word.upper()
            for swering in customList:
                if newWord == swering:
                    flag = True
                    break
            if flag:
                break

        return flag
