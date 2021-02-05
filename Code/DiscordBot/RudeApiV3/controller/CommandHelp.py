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
        print('Help module loaded successfully!')

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

        if arg.upper() == 'ALL':
            embed.add_field(name='Setting command',
                            value='**!modePenalty [on/off]**\tBy default the Penalty Mode is active.',
                            inline=False
                            )
            embed.add_field(name='Penalties commands',
                            value='**!setPenalty [user_id]=[new_faults_number]**\tChange the faults amount of a user.\n'
                            '**!curPenalty [user_id]**\tSee the actual fault instances previous to ban a member.\n'
                            '**!penalty [user_id]**\tAdd a penalty to a user.',
                            inline=False)
            embed.add_field(name='Stories commands',
                            value='**!userStory [user_id]**\tShow the faults story of a user.\n'
                            '**!cleanStory [user_id]**\tClean the faults story of a user.\n'
                            '**!undoStory [user_id]**\tRemove one fault to a user.\n'
                            '**!clrGlobalSty**\tClean everyone\'s faults story.',
                            inline=False)
            embed.add_field(name='Lists commands',
                            value='**!whitelist**\tSee guild whitelist.\n'
                            '**!wlAdd [user_id]**\t Add a user into the whitelist.\n'
                            '**!wlDel [user_id]**\t Delete a user from the whitelist.',
                            inline=False)
            embed.add_field(name='Custom Words commands',
                            value='**!addCustom**\tAdd a custom word.\n'
                            '**!rmvCustom**\tRemove a custom word.\n'
                            '**!addIgnore**\tAdd an ignored word.\n'
                            '**!rmvIgnore**\tRemove an ignored word.',
                            inline=False
                            )
            embed.add_field(name='Request command',
                            value='**!request [word],[language]**\tUpload a word to be added into the global banned words list.',
                            inline=False)
            embed.add_field(name='Bug command',
                            value='**!bug [text]**\tSend a bug report.',
                            inline=False)
        elif arg.upper() == 'SETTINGS':
            embed.add_field(name='Setting command',
                            value='**!modePenalty [on/off]**\tBy default the Penalty Mode is active.',
                            inline=False
                            )
            embed.add_field(name='Mode description',
                            value='**Penalty**\tWhen enabled, the Discord members will get warnings every time '
                            'they send offensive words in a chat. If someone got 5 warnings accumulated, they will be banned '
                            'automatically from the server. If it is disabled, the bot will only delete messages with offensive content.',
                            inline=False
                            )
        elif arg.upper() == 'PENALTIES':
            embed.add_field(name='Penalties commands',
                            value='**!setPenalty [user_id]=[new_faults_number]**\tChange the faults amount of a user.\n'
                            '**!curPenalty [user_id]**\tSee the actual fault instances previous to ban a member.\n'
                            '**!penalty [user_id]**\tAdd a penalty to a user.',
                            inline=False)
            embed.add_field(name='Faults amount',
                            value='This number can only be an integer, greater or equal to 0.',
                            inline=False
                            )
        elif arg.upper() == 'STORIES':
            embed.add_field(name='Stories commands',
                            value='**!userStory [user_id]**\tShow the faults story of a user.\n'
                            '**!cleanStory [user_id]**\tClean the faults story of a user.\n'
                            '**!undoStory [user_id]**\tRemove one fault to a user.\n'
                            '**!clrGlobalSty**\tClean everyone\'s faults story.',
                            inline=False)
            embed.add_field(name='Be careful',
                            value='There is no possibility of turning back accidental changes in the stories, '
                            'please be careful with your stories.',
                            inline=False
                            )
        elif arg.upper() == 'LISTS':
            embed.add_field(name='Lists commands',
                            value='**!whitelist**\tSee guild whitelist.\n'
                            '**!wlAdd [user_id]**\t Add a user into the whitelist.\n'
                            '**!wlDel [user_id]**\t Delete a user from the whitelist.\n',
                            inline=False)
        elif arg.upper() == 'CUSTOMS':
            embed.add_field(name='Custom Words commands',
                            value='**!addCustom**\tAdd a custom word.\n'
                            '**!rmvCustom**\tRemove a custom word.\n'
                            '**!addIgnore**\tAdd an ignored word.\n'
                            '**!rmvIgnore**\tRemove an ignored word.',
                            inline=False
                            )
            embed.add_field(name='Explanation',
                            value='**Custom words**\tWords that you can select to be banned.\n'
                            '**Ignored words**\tWords that you can select to be ignored.',
                            inline=False
                            )
            embed.add_field(name='Restrictions',
                            value='You can only have a maximum amount of 15 custom words and 15 ignored words.',
                            inline=False
                            )
        elif arg.upper() == 'REQUESTS':
            embed.add_field(name='Request command',
                            value='**!request [word],[language]**\tUpload a word to be added into the global banned words list.',
                            inline=False)
            embed.add_field(name='Language selection',
                            value='**en**\tEnglish.\n'
                            '**es**\tSpanish.\n'
                            '**may**\tMayan.',
                            inline=False)
            embed.add_field(name='Restrictions',
                            value='You can only make 5 requests per month.\n'
                            'You can\'t suggest existing words, in case you do, the bot will tell you '
                            'without any penalization.',
                            )
        elif arg.upper() == 'BUGS':
            embed.add_field(name='Bug command',
                            value='**!bug [text]**\tSend a bug report.',
                            inline=False)
            embed.add_field(name='Cooldown',
                            value='It is only possible to send one request per day.\n',
                            inline=False)
        else:
            embed.add_field(name='Arguments',
                            value='**!help**\tDisplays the list of options.\n'
                            '**!help all**\tDisplays all commands.\n'
                            '**!help settings**\tDisplays the setting command.\n'
                            '**!help penalties**\tDisplays penalties related commands.\n'
                            '**!help stories**\tDisplays stories related commands.\n'
                            '**!help lists**\tDisplays lists related commands.\n'
                            '**!help customs**\tDisplays custom words related commands\n'
                            '**!help requests**\tDisplays requesting command.\n'
                            '**!help bugs**\tDisplays bug reporting command.',
                            inline=False)
            embed.add_field(name='Tip',
                            value='Some commands have more information that cannot be seen with "!help all" command. '
                            'You can take a look into the other sections if you want to learn more about them.',
                            inline=False
                            )

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
