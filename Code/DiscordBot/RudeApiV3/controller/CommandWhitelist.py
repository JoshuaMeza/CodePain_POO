"""
Author CodePain Team
Date 05/02/2021
Version 1.0.0
Custom Words Module
"""
import discord
from discord.ext import commands
from Main import memory


class Whitelist(commands.Cog):
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
        print('Whitelist module loaded successfully!')

    # Commands
    @commands.command(alisases=['WHITELIST'])
    @commands.has_role('Rudebot Manager')
    async def whitelist(self, ctx):
        """
        """
        print()

    @commands.command(alisases=['WHITELIST'])
    @commands.has_role('Rudebot Manager')
    async def wlAdd(self, ctx):
        """
        """
        print()

    @commands.command(alisases=['WHITELIST'])
    @commands.has_role('Rudebot Manager')
    async def wlDel(self, ctx):
        """
        """
        print()


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Whitelist(client, memory))
