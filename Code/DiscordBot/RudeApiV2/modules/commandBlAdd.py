import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools

class BlAdd(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('BlAdd module loaded succesfully!')

	# Commands
	@commands.command(name=['blAdd'])
	async def command_blAdd(self, ctx, arg):
		ctx.send(self.tools.ModifyDatabase("banlist", arg, "add"))


def setup(client):
	client.add_cog(BlAdd(client))