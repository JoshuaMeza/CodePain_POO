"""
Author CodePain Team
Date 14/01/2021
Version 1.0.0
Request Module
"""
import discord
from discord.ext import commands
from Main import memory


class Request(commands.Cog):
    def __init__(self, client, memory):
        """
        This is a constructor
        """
        self.client = client
        self.memory = memory

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """
        When the bot gets activated, this function prints a message
        """
        print('Request module loaded succesfully!')

    # Commands
    @commands.command(aliases=['REQUEST'])
    @commands.has_role('Rudebot Manager')
    async def request(self, ctx, *, msg=""):
        """
        When a user send a request, verifies if he can still doing it and then send it to the database
        Args:
            self (object): The object itself
            ctx (object): Context
            embed (object): A Discord message type
            msg (str): Word to request
        Returns:
            Nothing
        """
        if msg != '':
            if self.memory.addRequest(ctx.author.id):
                await ctx.send('Request for "{}" was succesfully sent!'.format(msg))
            else:
                embed = discord.Embed(
                    title='Error!',
                    description='You can send a maximum of 5 requests per month',
                    colour=discord.Colour.from_rgb(225, 73, 150)
                )
                await ctx.send(embed=embed, delete_after=10.0)
        else:
            embed = discord.Embed(
                title='Error!',
                description='You need to write a word, type "!help requests" to get more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Request(client, memory))
