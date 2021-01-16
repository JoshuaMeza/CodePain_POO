import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools

class CurPenalty(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('CurPenalty module loaded succesfully!')

	# Commands
	@commands.command(aliases=['curPenalty'])
	async def command_curPenalty(self, ctx):
		Penalties = self.tools.CheckDatabase("penalty")
		ctx.send(self.tools.ListElements(Penalties, "List of Current Instances on the server"))

def setup(client):
	client.add_cog(CurPenalty(client))