import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools


class Admins(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('Admins module loaded succesfully!')

	# Commands
	@commands.command(aliases=['admins'])
	async def command_admins(self, ctx):
		adminList = self.tools.CheckDatabase("admins")
		ctx.send(self.tools.ListElements(adminList, "List of Admins"))


def setup(client):
	client.add_cog(Admins(client))