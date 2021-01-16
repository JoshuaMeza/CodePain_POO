"""
Author CodePain Team
Date 14/01/2021
Version 1.0.0
Searcher tool
"""


class Searcher:
    def __init__(self, connector):
        self.words = connector.returnWords()

    def searchWord(self, text):
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
