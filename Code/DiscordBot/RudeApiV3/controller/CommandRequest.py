"""
Author CodePain Team
Date 14/01/2021
Version 1.0.0
Request Module
"""
import discord
from discord.ext import commands
from Main import memory, connector, search


class Request(commands.Cog):
    def __init__(self, client, memory, connector, search):
        """
        This is a constructor
        """
        self.client = client
        self.memory = memory
        self.con = connector
        self.search = search

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """
        When the bot gets activated, this function prints a message
        """
        print('Request module loaded successfully!')

    # Commands
    @commands.command(aliases=['REQUEST'])
    @commands.has_role('Rudebot Manager')
    async def request(self, ctx, *, msg=''):
        """
        When a user send a request, verifies if he can still doing it and then send it to the database
        Args:
            self (object): The object itself
            ctx (object): Context
            embed (object): A Discord message type
            msg (str): Word to request
            content (list): Saves the word and the language
            langId (dict): It contains the id's for the chosen words
        Returns:
            Nothing
        """
        if msg != '':
            content = msg.split(',')
            if len(content) == 2:
                if (content[1] == 'en' or content[1] == 'es' or content[1] == 'may'):
                    if not self.search.searchWord(content[0]):
                        if self.memory.addRequest(ctx.author.id):
                            langId = {
                                'en': 1,
                                'es': 2,
                                'may': 3
                            }
                            if (self.con.sendRequest(content[0].upper(), langId[content[1]])):
                                await ctx.send('Request for "{}" was successfully sent!'.format(content[0]))
                        else:
                            embed = discord.Embed(
                                title='Validation Error',
                                description='You can send a maximum of 5 requests per month, type "!help requests" for more information.',
                                colour=discord.Colour.from_rgb(225, 73, 150)
                            )
                            await ctx.send(embed=embed, delete_after=10.0)
                    else:
                        embed = discord.Embed(
                            title='Validation Error',
                            description='You can\'t send an existing word, type "!help requests" for more information.',
                            colour=discord.Colour.from_rgb(225, 73, 150)
                        )
                        await ctx.send(embed=embed, delete_after=10.0)
                else:
                    embed = discord.Embed(
                        title='Argument Error',
                        description='Select a valid language, type "!help requests" for more information.',
                        colour=discord.Colour.from_rgb(225, 73, 150)
                    )
                    await ctx.send(embed=embed, delete_after=10.0)
            else:
                embed = discord.Embed(
                    title='Argument Error',
                    description='You need to write the needed parameters, type "!help requests" for more information.',
                    colour=discord.Colour.from_rgb(225, 73, 150)
                )
                await ctx.send(embed=embed, delete_after=10.0)
        else:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to write the needed parameters, type "!help requests" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Request(client, memory, connector, search))
