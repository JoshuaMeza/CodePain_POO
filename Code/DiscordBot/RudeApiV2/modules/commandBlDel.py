import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools

class BlDel(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('BlDel module loaded succesfully!')

	# Commands
	@commands.command(aliases=['blDel'])
	async def command_blDel(self, ctx, arg):
		ctx.send(self.tools.ModifyDatabase("banlist", arg, "del"))


def setup(client):
	client.add_cog(BlDel(client))