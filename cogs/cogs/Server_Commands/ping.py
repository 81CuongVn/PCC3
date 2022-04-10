import discord
from discord.ext import commands
from discord.ui import Button, View

class ping(commands.Cog):

    def __init__(self, client):
        self.client = client 



    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send(f'Pong\nLatency: **{self.client.latency*1000:,.0f}ms**')


    @commands.slash_command(name="ping", description="Will return the ping of the bot")
    async def ping_slash(self, ctx):
        await ctx.respond(f'Pong\nLatency: **{self.client.latency*1000:,.0f}ms**')


def setup(client):
    client.add_cog(ping(client))