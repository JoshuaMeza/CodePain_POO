"""
Author CodePain Team
Date 04/02/2021
Version 1.0.0
Managers Module
"""
import discord
from discord.ext import commands
from controller.Punisher import *
from discord.ext.commands import cooldown, BucketType
from Main import connector


class Managers(commands.Cog):
    def __init__(self, client, connector):
        """
        This is a constructor
        """
        self.client = client
        self.punisher = Punisher(connector)

    # Events

    @commands.Cog.listener()
    async def on_ready(self):
        """
        When the bot gets activated, this function prints a message
        """
        print('Managers module loaded successfully!')

    # Commands
    @commands.command(alisases=['KICK'])
    @commands.has_role('Rudebot Manager')
    @cooldown(1, 900, BucketType.user)
    async def kick(self, ctx, *, member: discord.User = None):
        """
        """
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot kick yourself!")
        else:
            await ctx.guild.kick(member, reason='You are too rude!')


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Managers(client, connector))
