import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools

class DelCmChannel(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('DelCmChannel module loaded succesfully!')

	# Commands
	@commands.command(aliases=['delCmChannel'])
	async def command_delCmChannel(self, ctx, arg):
		ctx.send(self.tools.ModifyDatabase("cmChannels", arg, "del"))

def setup(client):
	client.add_cog(DelCmChannel(client))