from discord.ext import commands
import discord, Stories, BotProtocols

token = "Nzg0MTUzMzYxMDU4MTAzMzA2.X8lJug.NXXW3J-Fo0iH_wXuJEDNyZddWQE"
client = discord.Client()
data = Stories.Stories()
protocol = BotProtocols.BotProtocols()
bot = commands.Bot(command_prefix="!")

@bot.command(name = "help")
async def command_help(ctx, arg = None):
	commands_channels = protocol.commandChannels
	# Check if in correct channel
	if str(ctx.channel) in commands_channels and len(commands_channels) > 0:
		if arg is not None:
			helpMsg = ""
			# ToDo formating messages
			if arg == "admins":
				helpMsg = "Type: !setAdmin to add another admin who can manage bot permissions. " \
				          "Type: !delAdmin to delete an admin." \
				          "Type: !admins to see a full list of admins."
			elif arg == "channels":
				helpMsg = "Type: !setCmChannels to add a channel to send bot commands" \
				          "Type: !delCmChannels to delete a channel that recieve bot commands" \
				          "Type: !cmChannels to see a full list of command channels" \
				          "Type: !setChannel to add a channel to constantly check messages" \
				          "Type: !delChanel to stop checking messages from a channel" \
				          "Type: !channels to se a full list of avtive channels"
			elif arg == "penalty":
				helpMsg = "Type: !setPenalty to change the faul instances previous to ban a member" \
				          "Type: !curPenalty to see the actual faul instances previous to ban a member" \
				          "Type: !penalty to add a faul to a member"

			elif arg == "stories":
				helpMsg = "Type: !showStories to see all faul stories from all registered users." \
				          "Type: !userStory to see if a user has an story." \
				          "Type: !clearStory to fully delete an user Story" \
				          "Type: !undoStory to remove a faul instance from a member"
			else:
				helpMsg = "Type: !whiteList to see the server whitelist" \
				          "Type: !banlist to see the servers own banned words" \
				          "Type: !wlAdd to add a member to the whitelist" \
				          "Type: !wlDel to delete a member from the whitelist" \
				          "Type: !blAdd to add a new word to the banlist" \
				          "Type: !blDel to delete a word from the banlist"
		else:
			helpMsg = "This is the help menu" \
			          "Type: '!help admins' to see admin related commands." \
			          "Type: '!help channels' to see channels related commands." \
			          "Type: '!help penalty' to see penalties related commands." \
			          "Type: '!help stories' to see stories related commands." \
			          "Type: '!help lists' to see banlist & whitelist related commands."
		await ctx.send(helpMsg)

#ToDo: remaining commands

#-----------------------------------Admin commands-------------------------------------------------
@bot.command(name = "setAdmin")
async def command_help(ctx, arg):
	pass
@bot.command(name = "delAdmin")
async def command_help(ctx, arg):
	pass
@bot.command(name = "admins")
async def command_help(ctx):
	pass

#----------------------------------- Common Channel commands---------------------------------------
#----------------------------------- Commands Channels commands -----------------------------------
#----------------------------------- Penalty commands ---------------------------------------------
#----------------------------------- Stories commands ---------------------------------------------
#----------------------------------- List commands ------------------------------------------------

@bot.command(name = "setpenalty")
async def command_help(ctx):
	pass

@client.event
async def on_message(message):
	channels = protocol.channels()
	if str(message.channel) in channels and len(channels) > 0:  # Check if in correct channel
		if protocol.checkmessage(message):
			data.newStory(message.author)
			#ToDo: Add ban method.
