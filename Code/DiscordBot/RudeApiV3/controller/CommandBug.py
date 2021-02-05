"""
Author CodePain Team
Date 02/02/2021
Version 1.0.0
Bug Report Module
"""
import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from Main import connector

class Bug(commands.Cog):
    def __init__(self, client, connector):
        """
        This is a constructor
        """
        self.client = client
        self.con = connector


    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """
        When the bot gets activated, this function prints a message
        """
        print('Bug report module loaded successfully!')

    # Commands
    @commands.command(alisases=['BUG', 'bugs', 'BUGS'])
    @commands.has_role('Rudebot Manager')
    @cooldown(1,86400,BucketType.user)
    async def bug(self, ctx, *, msg=""):
        """
        When a user send a request, verifies if he can still doing it and then send it to the database
        Args:
            self (object): The object itself
            ctx (object): Context
            msg (str): Report text
        Returns:
            Nothing
        """
        if msg != '':
            self.con.sendBugReport(msg,ctx.guild.id)
            await ctx.send('Bug report was successfully sent!')
        else:
            embed = discord.Embed(
                title='Error!',
                description='You need to write the report, type "!help bug" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)




def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Bug(client, connector))