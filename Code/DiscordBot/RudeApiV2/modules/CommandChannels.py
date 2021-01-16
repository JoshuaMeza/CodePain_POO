import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools


class Channels(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('Channels module loaded succesfully!')

	# Commands
	@commands.command(aliases=['channels'])
	async def command_channels(self, ctx):
		channels = self.tools.CheckDatabase("channels")
		ctx.send(self.tools.ListElements(channels, "List of Protected Channels"))

def setup(client):
	client.add_cog(Channels(client))