import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools

class Banlist(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('Banlist module loaded succesfully!')

	# Commands
	@commands.command(aliases=['banlist'])
	async def command_banlist(self, ctx):
		banlist = self.tools.CheckDatabase("banlist")
		ctx.send(self.tools.ListElements(banlist, "Words Banlist"))

def setup(client):
	client.add_cog(Banlist(client))