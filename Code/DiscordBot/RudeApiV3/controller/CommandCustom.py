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
    @commands.command(aliases=['addcustom', 'ADDCUSTOM'])
    @commands.has_role('Rudebot Manager')
    async def addCustom(self, ctx, *, msg=''):
        """
        This method adds a new custom word
        Args:
            self (object): The object itself
            ctx (object): Context
            msg (str): Custom word
            memory (object): Saver object
            embed (object): A Discord message type
        Returns:
            Nothing
        """
        if msg != '':
            if self.memory.customAmount(ctx.guild.id) != 15:
                if self.memory.addCustom(msg.upper(), ctx.guild.id):
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

    @commands.command(aliases=['delcustom', 'DELCUSTOM'])
    @commands.has_role('Rudebot Manager')
    async def delCustom(self, ctx, *, msg=''):
        """
        This method deletes a custom word
        Args:
            self (object): The object itself
            ctx (object): Context
            msg (str): Custom word
            memory (object): Saver object
            embed (object): A Discord message type
        Returns:
            Nothing
        """
        if msg != '':
            if self.memory.customAmount(ctx.guild.id) > 0:
                if self.memory.delCustom(msg.upper(), ctx.guild.id):
                    await ctx.send(f'Successfully deleted "{msg}".')
                else:
                    await ctx.send('The deletion failed.')
            else:
                embed = discord.Embed(
                    title='Validation Error',
                    description='Your guild can\'t have less than 0 custom words, type "!help customs" for more information.',
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

    @commands.command(aliases=['getcustom', 'GETCUSTOM'])
    @commands.has_role('Rudebot Manager')
    async def getCustom(self, ctx):
        """
        This method shows all custom words
        Args:
            self (object): The object itself
            ctx (object): Context
            guilds (dict): Guild dictionary of Custom Words
            memory (object): Saver object
            word (list): List of custom words
            words (str): A word
            output (str): List like a string
            embed (object): A Discord message type
        Returns:
            Nothing
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

    @commands.command(aliases=['addignore', 'ADDIGNORE'])
    @commands.has_role('Rudebot Manager')
    async def addIgnore(self, ctx, *, msg=''):
        """
        This method adds a new ignored word
        Args:
            self (object): The object itself
            ctx (object): Context
            msg (str): Ignored word
            memory (object): Saver object
            embed (object): A Discord message type
        Returns:
            Nothing
        """
        if msg != '':
            if self.memory.ignoredAmount(ctx.guild.id) != 15:
                if self.memory.addIgnored(msg.upper(), ctx.guild.id):
                    await ctx.send(f'Successfully added "{msg}".')
                else:
                    await ctx.send('The addition failed.')
            else:
                embed = discord.Embed(
                    title='Validation Error',
                    description='Your guild can only have a maximum amount of 15 ignored words, type "!help customs" for more information.',
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

    @commands.command(aliases=['delignore', 'DELIGNORE'])
    @commands.has_role('Rudebot Manager')
    async def delIgnore(self, ctx, *, msg=''):
        """
        This method deletes an ignored word
        Args:
            self (object): The object itself
            ctx (object): Context
            msg (str): Ignored word
            memory (object): Saver object
            embed (object): A Discord message type
        Returns:
            Nothing
        """
        if msg != '':
            if self.memory.ignoredAmount(ctx.guild.id) > 0:
                if self.memory.delIgnored(msg.upper(), ctx.guild.id):
                    await ctx.send(f'Successfully deleted "{msg}".')
                else:
                    await ctx.send('The deletion failed.')
            else:
                embed = discord.Embed(
                    title='Validation Error',
                    description='Your guild can\'t have less than 0 ignored words, type "!help customs" for more information.',
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

    @commands.command(aliases=['getignore', 'GETIGNORE'])
    @commands.has_role('Rudebot Manager')
    async def getIgnore(self, ctx):
        """
        This method shows all ignored words
        Args:
            self (object): The object itself
            ctx (object): Context
            guilds (dict): Guild dictionary of Ignored Words
            memory (object): Saver object
            word (list): List of ignored words
            words (str): A word
            output (str): List like a string
            embed (object): A Discord message type
        Returns:
            Nothing
        """
        guilds = self.memory.getIgnoredDict()
        words = guilds[str(ctx.guild.id)]
        output = ''

        for word in words:
            output += f'{word},'

        embed = None

        if output == '':
            embed = discord.Embed(
                title='Ignored words',
                description='Your guild does not have ignored words yet.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
        else:
            embed = discord.Embed(
                title='Ignored words',
                description='{}'.format(output[:-1]),
                colour=discord.Colour.from_rgb(225, 73, 150)
            )

        await ctx.send(embed=embed)


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Customs(client, memory))
