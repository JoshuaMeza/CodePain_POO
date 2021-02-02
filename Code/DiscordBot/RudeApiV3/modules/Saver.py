"""
Author CodePain Team
Date 14/01/2021
Version 1.0.0
Saver tool
"""


class Saver:
    def __init__(self):
        """
        This is a constructor
        """
        self.requestLog = []

    def verify(self, userId):
        """
        This method verifies if the user exist in the list
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
        This method adds a user to the list
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
        This method adds a user to the list
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
