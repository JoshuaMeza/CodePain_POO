import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools

class Penalty(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('Penalty module loaded succesfully!')

	# Commands
	@commands.command(aliases=['penalty'])
	async def command_penalty(self, ctx, arg):
		ctx.send(self.tools.ModifyDatabase("penalty", arg, "add"))

def setup(client):
	client.add_cog(Penalty(client))