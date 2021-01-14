import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools

class CmChannels(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('CmChannels module loaded succesfully!')

	# Commands
	@commands.command(aliases=['cmChannels'])
	async def command_cmChannels(self, ctx):
		CommandChannels =self.tools.CheckDatabase("cmChannels")
		ctx.send(self.tools.ListElements(CommandChannels, "List of Channels who admit admin commands"))

def setup(client):
	client.add_cog(CmChannels(client))