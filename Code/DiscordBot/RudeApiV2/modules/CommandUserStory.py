import discord
from discord.ext import commands
from RudeApiV2.modules.Stories import Stories

class UserStory(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.stories = Stories()

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('UserStory module loaded succesfully!')

	# Commands
	@commands.command(aliases=['userStory'])
	async def command_userStory(self, ctx, arg):
		ctx.send(self.stories.getStories(arg))

def setup(client):
	client.add_cog(UserStory(client))