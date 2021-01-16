"""
Author CodePain Team
Date 14/01/2021
Version 1.0.0
Saver tool
"""


class Saver:
    def __init__(self):
        self.requestLog = []

    def verify(self, userId):
        amount = 0
        if len(self.requestLog) != 0:
            for user in self.requestLog:
                if str(userId) == user[0]:
                    amount = user[1]
                    break
        return amount

    def addLog(self, userId):
        user = [str(userId), 0]
        self.requestLog.append(user)

    def increaseTimes(self, userId):
        for user in self.requestLog:
            if str(userId) == user[0]:
                user[1] += 1
                break

    def addRequest(self, userId):
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
