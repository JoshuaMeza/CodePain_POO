"""
Author CodePain Team
Date 06/02/2021
Version 1.0.0
API Module
"""
import discord
from discord.ext import commands
from Main import connector


class API(commands.Cog):
    def __init__(self, client, connector):
        """
        This is a constructor
        """
        self.client = client
        self.url = connector.returnUrl()

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """
        When the bot gets activated, this function prints a message
        """
        print('API module loaded successfully!')

    # Commands
    @commands.command(aliases=['api'])
    @commands.has_role('Rudebot Manager')
    async def API(self, ctx):
        """
        This method returns the API information.
        Args:
            self
            ctx
            embed
        Returns:
            Nothing
        """
        embed = discord.Embed(
            title='API',
            description='Main url: {}'.format(self.url),
            colour=discord.Colour.from_rgb(225, 73, 150)
        )

        embed.add_field(name='How to use it?',
                        value='[You can read more about it here.](https://github.com/JoshuaMeza/CodePain_POO/blob/master/Documentation/9-Accesing_API_documentation.md)',
                        inline=False
                        )

        await ctx.send(embed=embed)


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(API(client, connector))
