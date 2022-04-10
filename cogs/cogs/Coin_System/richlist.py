import discord
from discord.ext import commands
from discord import Option
from bank_functions import lead
import json

class richlist(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["richlist"])
    async def rich_command(self, ctx):
        send = ctx.send
        url=ctx.guild.icon.url
        await lead(send, url)

    @commands.slash_command(name="richlist", description="Who is the richest")
    async def rich_slash(self, ctx):
        send = ctx.respond
        url=ctx.guild.icon.url
        await lead(send, url)


def setup(client):
    client.add_cog(richlist(client)) 