from discord.ext import commands
import discord, Stories, BotProtocols



#------------------------------- Declarations -----------------------------------------------------
token = "Nzg0MTUzMzYxMDU4MTAzMzA2.X8lJug.NXXW3J-Fo0iH_wXuJEDNyZddWQE"
client = discord.Client()
data = Stories.Stories()
protocol = BotProtocols.BotProtocols()
bot = commands.Bot(command_prefix="!")



#-------------------------------- Commands -------------------------------------------------------
#--------------------------------Help Command ----------------------------------------------------
@bot.command(name = "help")
async def command_help(ctx, arg = None):
	#ToDo Format msgs
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		if arg is not None:
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


#-----------------------------------Admin commands-------------------------------------------------
@bot.command(name = "setAdmin")
async def command_setAdmin(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(arg + " succesfully added as admin!")

@bot.command(name = "delAdmin")
async def command_delAdmin(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		if protocol.removeAdmin(arg):
			ctx.send(arg + " succesfully removed from admin list!")
		else:
			ctx.send(arg + " is not in admin list!")

@bot.command(name = "admins")
async def command_admins(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.showAdmins())

#----------------------------------- Common Channel commands---------------------------------------
#ToDo Define Channels Commands.
@bot.command(name = "setChannel")
async def command_setChannel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageChannels("add", "default", arg)

@bot.command(name = "delChannel")
async def command_delChannel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author) and protocol.validateAdmin(ctx.author):
		protocol.manageChannels("remove", "default", arg)

@bot.command(name = "channels")
async def command_channels(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageChannels("show", "default")

#----------------------------------- Commands Channels commands -----------------------------------

#ToDo: Define Command Channels Commands.
@bot.command(name = "setCmChannel")
async def command_setCmChannel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageChannels("add", "command_channels", arg)

@bot.command(name = "delCmChannel")
async def command_delCmChannel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageChannels("remove", "command_channels", arg)

@bot.command(name = "cmChannels")
async def command_showCmChannels(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageChannels("remove", "command_channels")


#----------------------------------- Penalty commands ---------------------------------------------
#ToDo: Define Penalty Commands.
@bot.command(name = "setPenalty")
async def command_setPenalty(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.setPenaltyFlag(int(arg))

@bot.command(name = "curPenalty")
async def command_curPenalty(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.currentPenaltyFlag()

@bot.command(name = "penalty")
async def command_penalty(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		data.newStory(arg)

#----------------------------------- Stories commands ---------------------------------------------
#ToDo: Define Stories Commands.
@bot.command(name = "showStories")
async def command_showStories(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		data.getStories()

@bot.command(name = "userStory")
async def command_userStory(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		data.getStories(arg)

@bot.command(name = "clearStory")
async def command_clearStory(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		data.manageStories(arg, "delete")

@bot.command(name = "undoStory")
async def command_undoStory(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		data.manageStories(arg, "undo")

#----------------------------------- List commands ------------------------------------------------
#ToDo: Define Lists Commands.
@bot.command(name = "whitelist")
async def command_whitelist(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageLists("show", "whitelist")

@bot.command(name = "wlAdd")
async def command_wlAdd(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageLists("add", "whitelist", arg)

@bot.command(name = "wlDel")
async def command_wlDel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageLists("remove", "whitelist", arg)

@bot.command(name = "banlist")
async def command_banlist(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageLists("show", "banlist")

@bot.command(name = "blAdd")
async def command_blAdd(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageLists("add", "banlist", arg)

@bot.command(name = "blDel")
async def command_blDel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageLists("remove", "banlist", arg)


#-------------------------------------- bot events --------------------------------------------
@client.event
async def on_message(message):
	channels = protocol.channels()
	if str(message.channel) in channels or len(channels) == 0:  # Check if in correct channel
		if protocol.checkmessage(message):
			data.newStory(message.author)
			#ToDo: Add ban method.
