from discord.ext import commands
import discord, Stories, BotProtocols



#------------------------------- Declarations -----------------------------------------------------
with open('.env','r') as f:
    token = f.readline()
client = discord.Client()
data = Stories.Stories()
protocol = BotProtocols.BotProtocols()
bot = commands.Bot(command_prefix="!")



#-------------------------------- Commands -------------------------------------------------------
#--------------------------------Help Command ----------------------------------------------------
@bot.command(name = "help")
async def command_help(ctx, arg = None):
	#Tier 3 | ToDo: Give a cute format.
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		if arg is not None:
			if arg == "admins":
				helpMsg = "Type: !setAdmin to add another admin who can manage bot permissions.\n" \
				          "Type: !delAdmin to delete an admin.\n"\
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
				helpMsg = "Type: !whiteList to see the server whitelist.\n" \
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
			#tier 2 | ToDo: Simplify.

@bot.command(name = "admins")
async def command_admins(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.showAdmins())

#----------------------------------- Common Channel commands---------------------------------------
@bot.command(name = "setChannel")
async def command_setChannel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageChannels("add", "default", arg)
		ctx.send(arg + " succesfully added as a command channel.")

@bot.command(name = "delChannel")
async def command_delChannel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author) and protocol.validateAdmin(ctx.author):
		msg = protocol.manageChannels("remove", "default", arg)
		if msg:
			msg = arg +" removed from command channels."
		ctx.send(msg)
		#Tier 2 | ToDo: Simplify

@bot.command(name = "channels")
async def command_channels(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.manageChannels("show", "default")) #Tier 3 | ToDo: Give a cute format.

#----------------------------------- Commands Channels commands -----------------------------------
@bot.command(name = "setCmChannel")
async def command_setCmChannel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		protocol.manageChannels("add", "command_channels", arg)
		ctx.send(arg + " succesfully added as a moderation channel.")

@bot.command(name = "delCmChannel")
async def command_delCmChannel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		msg = protocol.manageChannels("remove", "command_channels", arg)
		if msg:
			msg = arg + " removed from command channels."
		ctx.send(msg)
		#Tier 2 | ToDo: Simplify

@bot.command(name = "cmChannels")
async def command_showCmChannels(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.manageChannels("show", "command_channels")) #Tier 3 | ToDo: Give a cute Format


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
@bot.command(name = "showStories")
async def command_showStories(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(data.getStories()) #Tier 2 | ToDo give a cute format

@bot.command(name = "userStory")
async def command_userStory(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(data.getStories(arg))

@bot.command(name = "clearStory")
async def command_clearStory(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(data.manageStories(arg, "delete"))

@bot.command(name = "undoStory")
async def command_undoStory(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(data.manageStories(arg, "undo"))

#----------------------------------- List commands ------------------------------------------------
#ToDo: Check.
@bot.command(name = "whitelist")
async def command_whitelist(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.manageLists("show", "whitelist"))

@bot.command(name = "wlAdd")
async def command_wlAdd(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.manageLists("add", "whitelist", arg))

@bot.command(name = "wlDel")
async def command_wlDel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.manageLists("remove", "whitelist", arg))

@bot.command(name = "banlist")
async def command_banlist(ctx):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.manageLists("show", "banlist"))

@bot.command(name = "blAdd")
async def command_blAdd(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.manageLists("add", "banlist", arg))

@bot.command(name = "blDel")
async def command_blDel(ctx, arg):
	if protocol.validateCmChannel(ctx) and protocol.validateAdmin(ctx.author):
		ctx.send(protocol.manageLists("remove", "banlist", arg))


#-------------------------------------- bot events --------------------------------------------
@client.event
async def on_message(message):
	channels = protocol.channels()
	if str(message.channel) in channels or len(channels) == 0:  # Check if in correct channel
		if protocol.checkmessage(message):
			data.newStory(message.author)
			#ToDo: Add ban method.
