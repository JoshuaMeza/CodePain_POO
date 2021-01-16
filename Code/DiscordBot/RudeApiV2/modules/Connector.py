"""
Author CodePain Team
Date 14/01/2021
Version 1.0.0
Connector tool
"""
import requests
import json

class Connector:
    def __init__(self):
        self.url = 'http://zivotmagazine.net/Pruebas/getAll.php'
        self.words = []
        self.getWords()

    def getWords(self):
        try:
            response = requests.get(self.url)
            temp = json.loads(response.content)
            for category in temp:
                for word in temp[category]:
                    self.words.append(word)
        except:
            self.words = None

    def returnWords(self):
        return self.words
