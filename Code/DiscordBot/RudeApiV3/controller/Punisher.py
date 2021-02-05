class Punisher:
    def __init__(self, connector):
        self.con = connector

    def punish(self, userId, guildId):
        story = self.con.getUserStory(userId, guildId)
        userWarnings = 0

        if (story is not None):
            userWarnings = int(story) + 1
            self.con.setUserStoryAmount(userId, guildId, userWarnings)
        else:
            userWarnings = 1
            self.con.addStory(userId, guildId)

        return userWarnings
