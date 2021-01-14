import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools

class Whitelist(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('Whitelist module loaded succesfully!')

	# Commands
	@commands.command(aliases=['whitelist'])
	async def command_whitelist(self, ctx, arg):
		whitelist = self.tools.CheckDatabase("whitelist")
		ctx.send(self.tools.ListElements(whitelist, "This is the Whitelist of the server"))

def setup(client):
	client.add_cog(Whitelist(client))