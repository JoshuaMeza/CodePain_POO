from RudeApiV2.modules import BotProtocols
from RudeApiV2.modules import Stories
from discord.ext import commands
import discord, os, sys



#------------------------------- Declarations -----------------------------------------------------
token = "Nzg0MTUzMzYxMDU4MTAzMzA2.X8lJug.Ep-6DoOagOFxg-OhnenDWRw-6t8"
client = discord.Client()
data = Stories.Stories()
protocol = BotProtocols.BotProtocols()
bot = commands.Bot(command_prefix="!")
bot.remove_command("help")


for filename in os.listdir('modules/'):
	if filename.endswith('.py') and 'Command' in filename:
		bot.load_extension('modules.{}'.format(filename[:-3]))


client.run(token)

#-------------------------------------- bot events --------------------------------------------
@client.event
async def on_ready():
	"""
	When the bot gets activated, this function prints a message
	"""
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	channels = protocol.channels()
	if str(message.channel) in channels or len(channels) == 0:  # Check if in correct channel
		if protocol.checkmessage(message):
			data.newStory(message.author)
			#ToDo: Add ban method.

	if message.content.startswith('!'):
		if protocol.validateCmChannel(message.channel) and protocol.validateAdmin(message.author):
			await bot.process_commands(message)
