import discord
from discord.ext import commands
from Main import *


class Dummy(commands.Cog):
    def __init__(self, client, system):
        self.client = client
        self.prefix = system


    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        # If this module is charged, will print it
        print('Say module loaded!')

    # Command
    @commands.command(aliases=['SAY'])
    async def say(self, ctx, *, msg=""):
        # Say the words that follow the command 
        await ctx.send(ctx.message.guild.id)
        

# Needed to initialize
def setup(client):
    client.add_cog(Dummy(client, system))