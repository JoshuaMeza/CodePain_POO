"""
Author CodePain Team
Date 01/01/2021
Version 1.2.0
A channel and chat management bot
"""
from modules.Saver import *
from modules.Connector import *
from modules.Searcher import *
import discord
import os
import sys
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv
# from keepAlive import *

# ------------------------------- Memory objects ---------------------------------------------------
memory = Saver()

# ------------------------------- Declarations -----------------------------------------------------
prefix = '!'
client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

# ------------------------------- Declarations -----------------------------------------------------
connector = Connector()
search = Searcher(connector)

# ------------------------------- Adding Extensions -------------------------------------------------
for filename in os.listdir('modules/'):
    if (filename.startswith('Command') and filename.endswith('.py')):
        client.load_extension('modules.{}'.format(filename[:-3]))


# ------------------------------- Bot events ---------------------------------------------------------
@client.event
async def on_ready():
    """
    When the bot gets activated, this function prints a message
    """
    print('We have logged in as {0.user}'.format(client))


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
        role = await guild.create_role(name='Rudebot Manager', colour=discord.Colour.from_rgb(225, 73, 150))

    if category is None:
        category = await guild.create_category_channel('Rudebot Management')
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(send_messages=False),
            guild.me: discord.PermissionOverwrite(send_messages=True),
            role: discord.PermissionOverwrite(send_messages=True)
        }
        await guild.create_text_channel('rude-admin', overwrites=overwrites, category=category)


@client.event
async def on_message(message):
    """
    This function gets activated when a user send a message
    Args:
        message (object): Represents the message
        search (object): Searcher object
    Returns:
        Nothing
    """
    if message.content == client.user:
        return
    elif message.content.startswith(prefix) and message.channel.name == 'rude-admin':
        await client.process_commands(message)
        return
    else:
        if search.searchWord(message.content):
            await message.delete()
            await message.author.send('You can\'t send swerings in {} server!'.format(message.guild.name))


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
            description='I don\'t recognize your command, try using {}help.'.format(
                prefix),
            colour=discord.Colour.from_rgb(225, 73, 150)
        )
        await ctx.send(embed=embed, delete_after=10.0)


# -------------------------------------- Initialization --------------------------------------------
# keep_alive()
load_dotenv()
client.run(os.getenv('TOKEN'))
