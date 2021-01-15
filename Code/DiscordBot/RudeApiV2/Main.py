"""
Author CodePain Team
Date 01/01/2021
Version 1.2.0
A channel and chat management bot
"""
from modules.BotProtocols import *
from modules.Stories import *
from modules.memory import *
import discord, os, sys
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
# from keepAlive import *

#------------------------------- Memory objects ----------------------------------------------------
# system = Dummy()

#------------------------------- Declarations -----------------------------------------------------
prefix = '!'
client = commands.Bot(command_prefix=prefix)
data = Stories()
protocol = BotProtocols()
client.remove_command('help')

#------------------------------- Adding Extensions -------------------------------------------------
for filename in os.listdir('modules/'):
    # if (filename.startswith('Command') and filename.endswith('.py')):
	if filename == 'CommandHelp.py' or filename == 'CommandAdministration.py':
		client.load_extension('modules.{}'.format(filename[:-3]))



#------------------------------- Bot events ---------------------------------------------------------
@client.event
async def on_ready():
	"""
	When the bot gets activated, this function prints a message
	"""
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	"""
	When someone sends a message, do the following
	Args:
		message (Object): Message sent
		channels (Object): Protocols
	Returns:
		Nothing
	"""
	if message.author == client.user:
		return
	
	if message.content.startswith('!') and message.channel.name == 'rude-admin':
		await client.process_commands(message)


@client.event
async def on_guild_join(guild):
	"""
	This function creates a channel and a role for managing the bot.
	Args:
		guild (object): Server
		flag (bool): Used to know if create or not
		role (class): Represents a role
		temp (class): Discord client
		overwrites (tupple): Save permissions
	Returns:
		Nothing
	"""
	role = get(guild.roles, name='Rudebot Manager')
	category = get(guild.categories, name='Rudebot Management')
	
	if role is None:
		role = await guild.create_role(name='Rudebot Manager',colour=discord.Colour.from_rgb(225,73,150))

	if category is None:
		category = await guild.create_category_channel('Rudebot Management')
		overwrites = {
			guild.default_role: discord.PermissionOverwrite(send_messages=False),
			guild.me: discord.PermissionOverwrite(send_messages=True),
			role: discord.PermissionOverwrite(send_messages=True)
		}
		await guild.create_text_channel('rude-admin', overwrites=overwrites, category=category)
		
		

	

@client.event
async def on_command_error(ctx, error):
    """
    This function sends a temporal message if a user tries to use an unknown command
    Args:
        ctx (object): Context
        error (object): Error found
    Returns:
        Nothing
    """
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title='Error!',
            description='I don\'t recognize your command, try using {}help.'.format(prefix),
            colour=discord.Colour.from_rgb(225,73,150)
        )
        await ctx.send(embed=embed, delete_after=10.0)


#-------------------------------------- Initialization --------------------------------------------
# keep_alive()
load_dotenv()
client.run(os.getenv('TOKEN'))
