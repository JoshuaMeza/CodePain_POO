import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools
from RudeApiV2.modules.Stories import Stories

class UndoStory(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.tools = Tools()
		self.stories = Stories()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('UndoStory module loaded succesfully!')

	# Commands
	@commands.command(aliases=['undoStory'])
	async def command_undoStory(self, ctx, arg):
		ctx.send(self.stories.manageStories(arg, "del"))

def setup(client):
	client.add_cog(UndoStory(client))