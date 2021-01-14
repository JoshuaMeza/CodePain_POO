import discord
from discord.ext import commands




class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """
        When the bot gets activated, this function prints a message
        """
        print('Help module loaded succesfully!')

    # Commands
    @commands.command(aliases=['help'])
    async def command_help(self, ctx, arg = None):
        """
       ToDo: Documentation
        """
        if arg is not None:
            if arg == "admins":
                helpMsg = "Type: !setAdmin to add another admin who can manage bot permissions.\n" \
                          "Type: !delAdmin to delete an admin.\n" \
                          "Type: !admins to see a full list of admins.\n"
            elif arg == "channels":
                helpMsg = "Type: !setCmChannels to add a channel to send bot commands.\n" \
                          "Type: !delCmChannels to delete a channel that recieve bot commands.\n" \
                          "Type: !cmChannels to see a full list of command channels.\n" \
                          "Type: !setChannel to add a channel to constantly check messages.\n" \
                          "Type: !delChanel to stop checking messages from a channel.\n" \
                          "Type: !channels to se a full list of avtive channels.\n"
            elif arg == "penalty":
                helpMsg = "Type: !setPenalty to change the faul instances previous to ban a member.\n" \
                          "Type: !curPenalty to see the actual faul instances previous to ban a member.\n" \
                          "Type: !penalty to add a faul to a member.\n"

            elif arg == "stories":
                helpMsg = "Type: !showStories to see all faul stories from all registered users.\n" \
                          "Type: !userStory to see if a user has an story.\n" \
                          "Type: !clearStory to fully delete an user Story.\n" \
                          "Type: !undoStory to remove a faul instance from a member.\n"
            else:
                helpMsg = "Type: !whitelist to see the server whitelist.\n" \
                          "Type: !banlist to see the servers own banned words.\n" \
                          "Type: !wlAdd to add a member to the whitelist\n" \
                          "Type: !wlDel to delete a member from the whitelist.\n" \
                          "Type: !blAdd to add a new word to the banlist.\n" \
                          "Type: !blDel to delete a word from the banlist.\n"
        else:
            helpMsg = "This is the help menu.\n" \
                      "Type: '!help admins' to see admin related commands.\n" \
                      "Type: '!help channels' to see channels related commands.\n" \
                      "Type: '!help penalty' to see penalties related commands.\n" \
                      "Type: '!help stories' to see stories related commands.\n" \
                      "Type: '!help lists' to see banlist & whitelist related commands.\n"
        await ctx.send(helpMsg)

def setup(client):
    client.add_cog(Help(client))