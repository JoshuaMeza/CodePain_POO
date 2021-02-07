"""
Author CodePain Team
Date 05/02/2021
Version 1.0.0
Whitelist Module
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
    @commands.command(aliases=['WHITELIST'])
    @commands.has_role('Rudebot Manager')
    async def whitelist(self, ctx):
        """
        This method shows the guilds whitelist
        Args:
        Returns:
        """
        guilds = self.memory.getWhiteList()
        users = guilds[str(ctx.guild.id)]
        output = ''

        for user in users:
            output += f'<@{user}>,'

        embed = None

        if output == '':
            embed = discord.Embed(
                title='Whitelist',
                description='Your guild does not have any member in your whitelist yet.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
        else:
            embed = discord.Embed(
                title='Whitelist',
                description='{}'.format(output[:-1]),
                colour=discord.Colour.from_rgb(225, 73, 150)
            )

        await ctx.send(embed=embed)

    @commands.command(aliases=['wladd', 'WLADD'])
    @commands.has_role('Rudebot Manager')
    async def wlAdd(self, ctx, *, userId=''):
        """
        This method adds a new user to the whitelist
        Args:
        Returns:
        """
        if userId != '':
            try:
                if ctx.guild.get_member(int(userId)) is not None:
                    if self.memory.whitelistAmount(ctx.guild.id) != 10:
                        if self.memory.addWhitelist(userId, ctx.guild.id):
                            await ctx.send(f'Successfully added <@{userId}> to the whitelist.')
                        else:
                            await ctx.send('The addition failed.')
                    else:
                        embed = discord.Embed(
                            title='Validation Error',
                            description='Your guild can only have a maximum amount of 10 whitelist members, type "!help lists" for more information.',
                            colour=discord.Colour.from_rgb(225, 73, 150)
                        )
                        await ctx.send(embed=embed, delete_after=10.0)
                else:
                    embed = discord.Embed(
                        title='Validation Error',
                        description='You entered an unknown member, type "!help lists" for more information.',
                        colour=discord.Colour.from_rgb(225, 73, 150)
                    )
                    await ctx.send(embed=embed, delete_after=10.0)
            except Exception:
                embed = discord.Embed(
                    title='Argument Error',
                    description='You need to specify a valid User ID, type "!help lists" for more information.',
                    colour=discord.Colour.from_rgb(225, 73, 150)
                )
                await ctx.send(embed=embed, delete_after=10.0)
        else:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to write the needed parameters, type "!help lists" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)

    @commands.command(aliases=['wldel', 'WLDEL'])
    @commands.has_role('Rudebot Manager')
    async def wlDel(self, ctx, *, userId=''):
        """
        This method adds a new user to the whitelist
        Args:
        Returns:
        """
        if userId != '':
            try:
                if ctx.guild.get_member(int(userId)) is not None:
                    if self.memory.whitelistAmount(ctx.guild.id) > 0:
                        if self.memory.delWhitelist(userId, ctx.guild.id):
                            await ctx.send(f'Successfully deleted <@{userId}> from the whitelist.')
                        else:
                            await ctx.send('The deletion failed.')
                    else:
                        embed = discord.Embed(
                            title='Validation Error',
                            description='Your guild can\'t have less than 0 whitelist members, type "!help lists" for more information.',
                            colour=discord.Colour.from_rgb(225, 73, 150)
                        )
                        await ctx.send(embed=embed, delete_after=10.0)
                else:
                    embed = discord.Embed(
                        title='Validation Error',
                        description='You entered an unknown member, type "!help lists" for more information.',
                        colour=discord.Colour.from_rgb(225, 73, 150)
                    )
                    await ctx.send(embed=embed, delete_after=10.0)
            except Exception:
                embed = discord.Embed(
                    title='Argument Error',
                    description='You need to specify a valid User ID, type "!help lists" for more information.',
                    colour=discord.Colour.from_rgb(225, 73, 150)
                )
                await ctx.send(embed=embed, delete_after=10.0)
        else:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to write the needed parameters, type "!help lists" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Whitelist(client, memory))
