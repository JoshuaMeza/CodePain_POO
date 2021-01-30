"""
Author CodePain Team
Date 14/01/2021
Version 1.0.0
Searcher tool
"""


class Searcher:
    def __init__(self, connector):
        """
        This is a constructor
        """
        self.words = connector.returnWordsList()

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
            for swering in self.words:
                if newWord == swering:
                    flag = True
                    break
            if flag:
                break
        return flag
