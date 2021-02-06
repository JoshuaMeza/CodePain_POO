"""
Author CodePain Team
Date 01/01/2021
Version 1.2.0
A channel and chat management bot
"""
from model.Saver import *
from model.Connector import *
from controller.Searcher import *
from controller.Punisher import *
from controller.KeepAlive import *
import discord
import os
import sys
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv


# ------------------------------- Declarations -----------------------------------------------------
intents = discord.Intents.default()
intents.members = True
prefix = '!'
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

# ------------------------------- Declarations -----------------------------------------------------
connector = Connector()
memory = Saver(connector)
search = Searcher(memory)
punisher = Punisher(connector)

# ------------------------------- Adding Extensions -------------------------------------------------
for filename in os.listdir('controller/'):
    if (filename.startswith('Command') and filename.endswith('.py')):
        client.load_extension('controller.{}'.format(filename[:-3]))


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
            guild.default_role: discord.PermissionOverwrite(send_messages=False, read_messages=False),
            guild.me: discord.PermissionOverwrite(send_messages=True, read_messages=True, administrator=True),
            role: discord.PermissionOverwrite(
                send_messages=True, read_messages=True)
        }
        await guild.create_text_channel('rude-admin', overwrites=overwrites, category=category)

    if (not connector.searchGuild(guild.id)):
        connector.recordGuild(guild.id)


@client.event
async def on_message(message):
    """
    This function gets activated when a user send a message
    Args:
        message (object): Represents the message
        search (object): Searcher object
        memory
        embed
        warnings
    Returns:
        Nothing
    """
    if message.author != client.user and not isinstance(message.channel, discord.channel.DMChannel):
        if message.content.startswith(prefix) and message.channel.name == 'rude-admin':
            await client.process_commands(message)
        elif search.searchWord(message.content, message.guild.id):
            await message.delete()

            if (memory.getSettings(message.guild.id) == 1):
                banFlag: False

                embed = discord.Embed(
                    title='Calm down my friend!',
                    description='You recently sent a message in **{}** that contains rudeness, and it is not allowed to use that type of vocabulary there.'.format(
                        message.guild.name),
                    colour=discord.Colour.from_rgb(225, 73, 150)
                )
                embed.add_field(
                    name='Message content',
                    value='"{}"'.format(message.content),
                    inline=False
                )

                warnings = punisher.punish(
                    message.author.id, message.guild.id)

                if warnings == 1:
                    banFlag = False
                    embed.add_field(
                        name='This is your fist warning!',
                        value='You have to know that if you reach an amount of 5 warnings, you will be automatically banned from the server.',
                        inline=False
                    )
                elif warnings < 5:
                    banFlag = False
                    embed.add_field(
                        name='You have {} warnings by now'.format(
                            warnings),
                        value='You have to know that if you reach an amount of 5 warnings, you will be automatically banned from the server.',
                        inline=False
                    )
                else:
                    banFlag = True
                    embed.add_field(
                        name='You have reached the maximum number of warnings',
                        value='I\'m sorry, but you were banned from the server.',
                        inline=False
                    )

                embed.add_field(
                    name='Did I do a mistake?',
                    value='Try to contact someone with **Rudebot Manager** role to verify your situation.',
                    inline=False
                )

                await message.author.send(embed=embed)

                if (not banFlag):
                    embed = discord.Embed(
                        title='{} has been warned in {}.'.format(
                            message.author.name, message.guild.name),
                        description='Message: {}'.format(message.content),
                        colour=discord.Colour.from_rgb(225, 73, 150)
                    )
                else:
                    await message.guild.ban(message.author, reason='You are too rude!', delete_message_days=7)
                    embed = discord.Embed(
                        title='{} has been banned in {}.'.format(
                            message.author.name, message.guild.name),
                        description='Message content: "{}"'.format(
                            message.content),
                        colour=discord.Colour.from_rgb(225, 73, 150)
                    )

                embed.add_field(name='Faults amount',
                                value='{} has {} faults in {}.'.format(
                                    message.author.name, warnings, message.guild.name),
                                inline=False
                                )

                for role in message.guild.roles:
                    if role.name == 'Rudebot Manager':
                        for member in role.members:
                            if member.id == client.user.id:
                                continue
                            await member.send(embed=embed)
                        break


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
    embed = None

    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title='Command Error',
            description='I don\'t recognize your command, try using {}help.'.format(
                prefix),
            colour=discord.Colour.from_rgb(225, 73, 150)
        )
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(
            title='Cooldown Error',
            description='This command is on cooldown, try again later.\nCheck the documentation for more information.',
            colour=discord.Colour.from_rgb(225, 73, 150)
        )
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title='Permissions Error',
            description='You don\'t have enough permissions to execute that command.',
            colour=discord.Colour.from_rgb(225, 73, 150)
        )
    else:
        embed = discord.Embed(
            title='Undefined Error',
            description='Something unexpected happend...',
            colour=discord.Colour.from_rgb(225, 73, 150)
        )
        print(error)

    await ctx.send(embed=embed, delete_after=10.0)


# -------------------------------------- Initialization --------------------------------------------
# keep_alive()
load_dotenv()
client.run(os.getenv('TOKEN'))
