"""
Author CodePain Team
Date 05/02/2021
Version 1.0.0
Stories Module
"""
import discord
from discord.ext import commands
from controller.Punisher import *
from Main import connector


class Stories(commands.Cog):
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
        print('Stories module loaded successfully!')

    # Commands
    @commands.command(aliases=['userstory', 'USERSTORY'])
    @commands.has_role('Rudebot Manager')
    async def userStory(self, ctx, *, userId=''):
        """
        This method sends the amount of warnings which a user has
        Args:
            self
            ctx
            userId
            flagResult
            punisher
            warnings
            embed
        Returns:
            Nothing
        """
        flagResult = False

        if userId != '':
            if ctx.guild.get_member(int(userId)) is not None:
                warnings = self.punisher.getPunishments(userId, ctx.guild.id)

                if warnings is None:
                    warnings = 0

                if warnings == 1:
                    await ctx.send('<@{}> has {} warning.'.format(userId, warnings))
                else:
                    await ctx.send('<@{}> has {} warnings.'.format(userId, warnings))

                flagResult = True

        if not flagResult:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to specify a valid User ID, type "!help stories" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)

    @commands.command(aliases=['cleanstory', 'CLEANSTORY'])
    @commands.has_role('Rudebot Manager')
    async def cleanStory(self, ctx, *, userId=''):
        """
        This method removes all the warnings of a user
        Args:
            self
            ctx
            userId
            flagResult
            punisher
            embed
        Returns:
            Nothing
        """
        flagResult = False

        if userId != '':
            if ctx.guild.get_member(int(userId)) is not None:
                if self.punisher.setPunishments(userId, ctx.guild.id, 0):
                    await ctx.send('<@{}>\'s story successfully cleaned.'.format(userId))
                else:
                    await ctx.send('Failed while trying to clean {}\'s story.'.format(userId))

                flagResult = True

        if not flagResult:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to specify a valid User ID, type "!help stories" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)

    @commands.command(aliases=['undostory', 'UNDOSTORY'])
    @commands.has_role('Rudebot Manager')
    async def undoStory(self, ctx, *, userId=''):
        """
        This method removes all the warnings of a user
        Args:
            self
            ctx
            userId
            flagResult
            punisher
            embed
        Returns:
            Nothing
        """
        flagResult = False

        if userId != '':
            if ctx.guild.get_member(int(userId)) is not None:
                num = int(self.punisher.getPunishments(userId, ctx.guild.id))

                if num != 0:
                    self.punisher.setPunishments(userId, ctx.guild.id, num - 1)

                await ctx.send('Successfully undone one fault of <@{}>.'.format(userId))

                flagResult = True

        if not flagResult:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to specify a valid User ID, type "!help stories" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)

    @commands.command(aliases=['clrglobalsty', 'CLRGLOBALSTY'])
    @commands.has_role('Rudebot Manager')
    async def clrGlobalSty(self, ctx):
        """
        This method cleans the entire story of a guild
        Args:
            self
            ctx
            punisher
        Returns:
            Nothing
        """
        if self.punisher.forgive(ctx.guild.id):
            await ctx.send('@everyone has been forgiven.')
        else:
            await ctx.send('I failed forgiving @everyone.')


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Stories(client, connector))
