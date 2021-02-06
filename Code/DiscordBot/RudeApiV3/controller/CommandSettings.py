"""
Author CodePain Team
Date 04/02/2021
Version 1.0.0
Settings Module
"""
import discord
from discord.ext import commands
from Main import memory


class Settings(commands.Cog):
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
        print('Settings module loaded successfully!')

    # Commands
    @commands.command(aliases=['modepenalty', 'MODEPENALTY'])
    @commands.has_role('Rudebot Manager')
    async def modePenalty(self, ctx, *, msg=''):
        """
        This command changes the penalize mode
        Args:
            self
            ctx
            msg
            memory
            embed
        Returns:
            Nothing
        """
        if msg != '':
            if msg.upper() == 'ON':
                if self.memory.setSettings(ctx.guild.id, 1):
                    await ctx.send('Penalize mode successfully changed to **ON**.')
                else:
                    await ctx.send('Sorry, mode change failed.')
            elif msg.upper() == 'OFF':
                if self.memory.setSettings(ctx.guild.id, 0):
                    await ctx.send('Penalize mode successfully changed to **OFF**.')
                else:
                    await ctx.send('Sorry, mode change failed.')
            else:
                embed = discord.Embed(
                    title='Argument Error',
                    description='You need to specify **on** or **off** value, type "!help settings" for more information.',
                    colour=discord.Colour.from_rgb(225, 73, 150)
                )
                await ctx.send(embed=embed, delete_after=10.0)
        else:
            embed = discord.Embed(
                title='Argument Error',
                description='You need to specify **on** or **off** value, type "!help settings" for more information.',
                colour=discord.Colour.from_rgb(225, 73, 150)
            )
            await ctx.send(embed=embed, delete_after=10.0)


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Settings(client, memory))
