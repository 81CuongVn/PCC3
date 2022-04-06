import discord
from discord.ext import commands
from discord import Option

class ping_bot_problem(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="bot_problem", description="Only if the Bot has major problems")
    async def ping_bot_problem(self, ctx, reason: Option(str, required = True)):
        embed = discord.Embed(title=None, description=reason, color=13565696)
        await ctx.respond(f"<@&951207540472029195>", embed=embed)
    


def setup(client):
    client.add_cog(ping_bot_problem(client))