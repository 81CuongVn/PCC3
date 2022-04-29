import discord
from discord.ext import commands
from discord import Option
from bank_functions import balance_command
import json

class balance(commands.Cog):

    def __init__(self, client):
        self.client = client


    #@commands.command(aliases=["balance", "bal", "coins"])
    #async def bal_normal_command(self, ctx, member:discord.Member = None):
    #    if member == None:
    #      member = ctx.author
    #    send = ctx.send
    #    await balance_command(ctx, send, member)


    @commands.slash_command(name="balance", description="Displays how much money you own")
    async def bal_slash_command(self, ctx, member: Option(discord.Member, required = False)):
        if member == None:
            member = ctx.author
        send = ctx.respond
        await balance_command(ctx, send, member)


def setup(client):
    client.add_cog(balance(client)) 