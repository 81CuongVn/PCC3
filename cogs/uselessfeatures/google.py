import discord
from discord.ext import commands
from discord import Option
import json
from googlesearch import search 

class google(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="google")
    async def find(self, ctx,*, query):
        async with ctx.typing():
            for i in search(query, lang="en", num_results=1):
                await ctx.send(f"{i}")

    @commands.slash_command(name="google", description="Just google things")
    async def find_slash(self, ctx, search: Option(str)):
        async with ctx.typing():
            for i in search(search, lang="en", num_results=1):
                await ctx.respond(f"{i}")               


def setup(client):
    client.add_cog(google(client)) 