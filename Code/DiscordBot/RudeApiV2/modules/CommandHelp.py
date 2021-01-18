"""
Author CodePain Team
Date 14/01/2021
Version 1.0.0
Help Module
"""
import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        """
        This is a constructor
        """
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        """
        When the bot gets activated, this function prints a message
        """
        print('Help module loaded succesfully!')

    # Commands
    @commands.command(name='help', alisases=['HELP', 'info', 'INFO'])
    @commands.has_role('Rudebot Manager')
    async def command_help(self, ctx, *, arg=''):
        """
        This method displays a help message
        Args:
            self (object): The object itself
            ctx (object): Context
            embed (object): A Discord message type
            arg (str): Argument
        Returns:
            Nothing
        """
        embed = discord.Embed(
            title='Help command',
            description='Note: Only people with "Rudebot Manager" role have permission to use my commands.',
            colour=discord.Colour.from_rgb(225, 73, 150)
        )

        if arg == 'all':
            embed.add_field(name='Channels commands',
                            value='**!addChannel [channel_id]**\tAdd protection to a given channel (by default all channels have protection).\n'
                            '**!deleteChannel [channel_id]**\tRemove protection to a given channel.',
                            inline=False)
            embed.add_field(name='Penalties commands',
                            value='**!setPenalty [user_id]=[new_faults_number]**\tChange the fauls amount of a user.\n'
                            '**!curPenalty [user_id]**\tSee the actual faul instances previous to ban a member.\n'
                            '**!penalty [user_id]**\tAdd a penalty to a user.',
                            inline=False)
            embed.add_field(name='Stories commands',
                            value='**!showStories**\tShow the stories of all guild members.\n'
                            '**!userStory [user_id]**\tShow the story of a user.\n'
                            '**!clearStory [user_id]**\tClean the complete story of a user.\n'
                            '**!undoStory [user_id]**\tRemove one faul to a user.',
                            inline=False)
            embed.add_field(name='List commands',
                            value='**!whitelist**\tSee guild whitelist.\n'
                            '**!wlAdd [user_id]**\t Add a user into the whitelist.\n'
                            '**!wlDel [user_id]**\t Delete a user from the whitelist.\n'
                            '**!banList**\tSee guild\'s banned users.\n'
                            '**!gwList**\tSee global banned words list.',
                            inline=False)
            embed.add_field(name='Request command',
                            value='**!request [word]**\tUpload a word to be added into the global banned words list.',
                            inline=False)
        elif arg == 'channels':
            embed.add_field(name='Channels commands',
                            value='**!addChannel [channel_id]**\tAdd protection to a given channel (by default all channels have protection).\n'
                            '**!deleteChannel [channel_id]**\tRemove protection to a given channel.',
                            inline=False)
        elif arg == 'penalties':
            embed.add_field(name='Penalties commands',
                            value='**!setPenalty [user_id]=[new_faults_number]**\tChange the fauls amount of a user.\n'
                            '**!curPenalty [user_id]**\tSee the actual faul instances previous to ban a member.\n'
                            '**!penalty [user_id]**\tAdd a penalty to a user.',
                            inline=False)
        elif arg == 'stories':
            embed.add_field(name='Stories commands',
                            value='**!showStories**\tShow the stories of all guild members.\n'
                            '**!userStory [user_id]**\tShow the story of a user.\n'
                            '**!clearStory [user_id]**\tClean the complete story of a user.\n'
                            '**!undoStory [user_id]**\tRemove one faul to a user.',
                            inline=False)
        elif arg == 'lists':
            embed.add_field(name='List commands',
                            value='**!whitelist**\tSee guild whitelist.\n'
                            '**!wlAdd [user_id]**\t Add a user into the whitelist.\n'
                            '**!wlDel [user_id]**\t Delete a user from the whitelist.\n'
                            '**!banList**\tSee guild\'s banned users.\n'
                            '**!gwList**\tSee global banned words list.',
                            inline=False)
        elif arg == 'requests':
            embed.add_field(name='Request command',
                            value='**!request [word]**\tUpload a word to be added into the global banned words list.',
                            inline=False)
        else:
            embed.add_field(name='Arguments',
                            value='**!help**\tDisplays the list of arguments.\n'
                            '**!help all**\tDisplays all commands.\n'
                            '**!help admins**\tDisplays administrators related commands.\n'
                            '**!help channels**\tDisplays channels related commands.\n'
                            '**!help penalties**\tDisplays penalties related commands.\n'
                            '**!help stories**\tDisplays stories related commands.\n'
                            '**!help lists**\tDisplays lists related commands.\n'
                            '**!help requests**\tDisplays requesting command.',
                            inline=False)

        embed.add_field(name='Documentation',
                        value='You can read more about me here:\nhttps://github.com/JoshuaMeza/CodePain_POO.',
                        inline=False)
        embed.set_image(
            url='https://github.com/JoshuaMeza/CodePain_POO/blob/master/Resources/RudeApiLogo.png?raw=true')
        embed.set_footer(text='CodePain Team')

        await ctx.message.add_reaction('👍')
        await ctx.send(embed=embed)


def setup(client):
    """
    Function needed to load the extension
    """
    client.add_cog(Help(client))
