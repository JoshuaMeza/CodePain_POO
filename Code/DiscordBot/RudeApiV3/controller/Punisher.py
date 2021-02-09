"""
Author CodePain Team
Date 04/02/2021
Version 1.0.0
Manages in great part the punishment backend
"""


class Punisher:
    def __init__(self, connector):
        """
        This is a constructor
        """
        self.con = connector

    def punish(self, userId, guildId):
        """
        This method adds a fault to a user
        Args:
            self (object): The object itself
            userId: (int): User ID
            guildId (int): Guild ID
            story (str): Warnings amount from database
            con (object): Connector object
            userWarnings (int): Warnings amount
        Returns:
            The amount of warnings
        """
        story = self.con.getUserStory(userId, guildId)
        userWarnings = 0

        if story is not None:
            userWarnings = int(story) + 1
            self.con.setUserStoryAmount(userId, guildId, userWarnings)
        else:
            userWarnings = 1
            self.con.addStory(userId, guildId)

        return userWarnings

    def setPunishments(self, userId, guildId, newFaultsNumber):
        """
        This method sets a custom amount of punishments
        Args:
            self (object): The object itself
            userId: (int): User ID
            guildId (int): Guild ID
            newFaultsNumber (str): New faults amount
            story (str): Warnings amount from database
            con (object): Connector object
        Returns:
            True if success, False if not
        """
        story = self.con.getUserStory(userId, guildId)

        if story is None:
            self.con.addStory(userId, guildId)

        return self.con.setUserStoryAmount(userId, guildId, newFaultsNumber)

    def getPunishments(self, userId, guildId):
        """
        This method returns the warnings of a user
        Args:
            self (object): The object itself
            userId: (int): User ID
            guildId (int): Guild ID
            con (object): Connector object
        Returns:
            The warnings which a user has
        """
        return self.con.getUserStory(userId, guildId)

    def forgive(self, guildId):
        """
        This function resets all the stories on a guild
        Args:
            self (object): The object itself
            guildId (int): Guild ID
            con (object): Connector object
        Returns:
            True if success, False if not
        """
        return self.con.resetGlobalStory(guildId)
