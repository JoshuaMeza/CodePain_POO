"""
Author CodePain Team
Date 04/02/2021
Version 1.0.0
Penalties Module
"""
import discord
from discord.ext import commands
from controller.Punisher import *
from Main import connector


class Penalties(commands.Cog):
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
        print('Penalties module loaded successfully!')

    # Commands
    @commands.command(aliases=['setpenalty', 'SETPENALTY'])
    @commands.has_role('Rudebot Manager')
    async def setPenalty(self, ctx, *, msg=''):
        """
        This method sets a new amount of fauls
        Args:
            self
            ctx
            msg
            info
            punisher
            embed
            flagResult
            userId
            num
        Returns:
            Nothing
        """
        if msg != '':
            info = msg.split('=')
            flagResult = False

            try:
                userId = int(info[0])
                num = int(info[1])

                if num >= 0:
                    if ctx.guild.get_member(userId) is not None:
                        if self.punisher.setPunishments(userId, ctx.guild.id, num):
                            await ctx.send('Successfully settled up {} fauls to <@{}>.'.format(num, userId))

                            if num >= 5:
                                await ctx.guild.ban(ctx.author, reason='You are too rude!', delete_message_days=7)

                            flagResult = True
                        else:
                            await ctx.send('The fauls change failed.')
                            flagResult = True
            except Exception as e:
                flagResult = False

            if not flagResult:
                embed = discord.Embed(
                    title='Argument Error',
                    description='You need to specify a valid User ID and a number, type "!help penalties" for more information.',
                    colour=discord.Colour.from_rgb(225, 73, 150)
                )
                await ctx.send(embed=embed, delete_after=10.0)

    @commands.command(aliases=['curpenalty', 'CURPENALTY'])
    @commands.has_role('Rudebot Manager')
    async def curPenalty(self, ctx, *, userId=''):
        """
        This method sends the amount of warnings until getting banned
        Args:
            self
            ctx
            userId
            flagResult
            punisher
            warnings
            final
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

                final = 5 - int(warnings)

                if final == 1:
                    await ctx.send('<@{}> has only {} warning left.'.format(userId, final))
                else:
                    await ctx.send('<@{}> has only {} warnings left.'.format(userId, final))

                flagResult = True

        if not flagResult:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to specify a valid User ID, type "!help stories" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)

    @commands.command(aliases=['PENALTY'])
    @commands.has_role('Rudebot Manager')
    async def penalty(self, ctx, *, userId=''):
        """
        This method adds a fault to a user
        Args:
            self
            ctx
            userId
            flagResult
            punisher
            embed
        """
        flagResult = False

        if userId != '':
            if ctx.guild.get_member(int(userId)) is not None:

                self.punisher.punish(userId, ctx.guild.id)

                await ctx.send('<@{}> got successfully penalized.'.format(userId))
                flagResult = True

        if not flagResult:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to specify a valid User ID, type "!help penalties" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Penalties(client, connector))
