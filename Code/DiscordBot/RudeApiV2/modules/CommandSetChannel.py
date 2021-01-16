import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools


class SetChannel(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()
	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('SetChannel module loaded succesfully!')

	# Commands
	@commands.command(aliases=['setChannel'])
	async def command_setChannel(self, ctx, arg):
		ctx.send(self.tools.ModifyDatabase("channels", arg, "add"))

def setup(client):
	client.add_cog(SetChannel(client))