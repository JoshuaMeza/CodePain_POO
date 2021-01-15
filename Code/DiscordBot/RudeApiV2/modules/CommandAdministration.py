import discord
from discord.ext import commands
from discord.utils import get

class AdminCommands(commands.Cog):
	def __init__(self, client):
		self.client = client
		self.embedError = discord.Embed(title='Error!',description='User not found.',colour=discord.Colour.from_rgb(225,73,150))

	# Events
	@commands.Cog.listener()
	async def on_ready(self):
		"""
		When the bot gets activated, this function prints a message
		"""
		print('Administration module loaded succesfully!')

    # Commands
	@commands.command(alisases=['SETADMIN'])
	@commands.has_role('Rudebot Manager')
	async def setAdmin(self, ctx, user: discord.Member):
		role = get(ctx.message.guild.roles, name='Rudebot Manager')

		await user.add_roles(role)
		await ctx.send('Succesfully added {} role to {}.'.format(role.mention,user.mention))

		

	@commands.command(alisases=['DELADMIN'])
	@commands.has_role('Rudebot Manager')
	async def delAdmin(self, ctx, user: discord.Member):
		role = get(ctx.message.guild.roles, name='Rudebot Manager')

		await ctx.author.remove_roles(role)
		await ctx.send('Succesfully removed {} role from {}.'.format(role.mention,user.mention))


def setup(client):
	client.add_cog(AdminCommands(client))