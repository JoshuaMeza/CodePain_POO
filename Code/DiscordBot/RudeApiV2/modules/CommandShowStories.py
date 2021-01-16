import discord
from discord.ext import commands
from RudeApiV2.modules.Tools import Tools
from RudeApiV2.modules.Stories import Stories


class ShowStories(commands.Cog):
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
		print('ShowStories module loaded succesfully!')

	# Commands
	@commands.command(aliases=['showStories'])
	async def command_showStories(self, ctx):
		stories = self.stories.getStories()
		ctx.send(self.tools.ListElements(stories, "list of all users with at least one story on this server"))

def setup(client):
	client.add_cog(ShowStories(client))