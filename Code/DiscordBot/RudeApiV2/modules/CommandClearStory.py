import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools

class ClearStory(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('ClearStory module loaded succesfully!')

	# Commands
	@commands.command(aliases=['clearStory'])
	async def command_clearStory(self, ctx, arg):
		ctx.send(self.tools.ModifyDatabase("banlist", arg, "cls"))

def setup(client):
	client.add_cog(ClearStory(client))