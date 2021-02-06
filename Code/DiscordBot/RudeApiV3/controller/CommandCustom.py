"""
Author CodePain Team
Date 05/02/2021
Version 1.0.0
Custom Words Module
"""
import discord
from discord.ext import commands
from Main import memory


class Customs(commands.Cog):
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
        print('Custom Words module loaded successfully!')

    # Commands
    @commands.command(alisases=['addcustom', 'ADDCUSTOM'])
    @commands.has_role('Rudebot Manager')
    async def addCustom(self, ctx, *, msg=''):
        """
        This method adds a new custom word
        """
        if msg != '':
            if self.memory.customAmount(ctx.guild.id) != 15:
                temp = msg.upper()
                if self.memory.addCustom(temp, ctx.guild.id):
                    await ctx.send(f'Successfully added "{msg}".')
                else:
                    await ctx.send('The addition failed.')
            else:
                embed = discord.Embed(
                    title='Validation Error',
                    description='Your guild can only have a maximum amount of 15 custom words, type "!help customs" for more information.',
                    colour=discord.Colour.from_rgb(225, 73, 150)
                )
                await ctx.send(embed=embed, delete_after=10.0)
        else:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to write the needed parameters, type "!help customs" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)

    @commands.command(alisases=['delcustom', 'DELCUSTOM'])
    @commands.has_role('Rudebot Manager')
    async def delCustom(self, ctx, *, msg=''):
        """
        This method deletes a custom word
        """
        if msg != '':
            if self.memory.customAmount(ctx.guild.id) > 0:
                temp = msg.upper()
                if self.memory.delCustom(temp, ctx.guild.id):
                    await ctx.send(f'Successfully deleted "{msg}".')
                else:
                    await ctx.send('The deletion failed.')
            else:
                embed = discord.Embed(
                    title='Validation Error',
                    description='You can\'t have less than 0 words, type "!help customs" for more information.',
                    colour=discord.Colour.from_rgb(225, 73, 150)
                )
                await ctx.send(embed=embed, delete_after=10.0)
        else:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to write the needed parameters, type "!help customs" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)

    @commands.command(alisases=['getcustom', 'GETCUSTOM'])
    @commands.has_role('Rudebot Manager')
    async def getCustom(self, ctx):
        """
        This method shows all custom words
        """
        guilds = self.memory.getCustomDict()
        words = guilds[str(ctx.guild.id)]
        output = ''

        for word in words:
            output += f'{word},'

        embed = None

        if output == '':
            embed = discord.Embed(
                title='Custom words',
                description='Your guild does not have custom words yet.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
        else:
            embed = discord.Embed(
                title='Custom words',
                description='{}'.format(output[:-1]),
                colour=discord.Colour.from_rgb(225, 73, 150)
            )

        await ctx.send(embed=embed)

    @commands.command(alisases=['addignore', 'ADDIGNORE'])
    @commands.has_role('Rudebot Manager')
    async def addIgnore(self, ctx):
        """
        """
        print()

    @commands.command(alisases=['delignore', 'DELIGNORE'])
    @commands.has_role('Rudebot Manager')
    async def delIgnore(self, ctx):
        """
        """
        print()

    @commands.command(alisases=['getignore', 'GETIGNORE'])
    @commands.has_role('Rudebot Manager')
    async def getIgnore(self, ctx):
        """
        """
        print()


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Customs(client, memory))
