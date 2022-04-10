import discord
from discord.ext import commands

class credit(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="credits")
    async def credit(self, ctx):
       async def credit_slash(self, ctx):
        embed = discord.Embed(title="Credits", color=13565696)
        embed.add_field(name="Bot Owner/Developer", value="<@695229647021015040>", inline=False)
        embed.add_field(name="Bot Developer", value="<@713696771188195368> \n<@443769343138856961>", inline=False)
        embed.add_field(name="Scores sheets", value="<@695229647021015040> \n<@713696771188195368>", inline=False)
        embed.add_field(name="Coin system", value="<@695229647021015040> \n<@443769343138856961> \n<@713696771188195368>", inline=False)
        embed.add_field(name="Coin system help (ideas etc.)", value="<@761937966867152929>", inline=False)

        await ctx.send(embed=embed)


    @commands.slash_command(name="credits", description="Shows bot developer(s)/owner")
    async def credit_slash(self, ctx):
        embed = discord.Embed(title="Credits", color=13565696)
        embed.add_field(name="Bot Owner/Developer", value="<@695229647021015040>", inline=False)
        embed.add_field(name="Bot Developer", value="<@713696771188195368> \n<@443769343138856961>", inline=False)
        embed.add_field(name="Scores sheets", value="<@695229647021015040> \n<@713696771188195368>", inline=False)
        embed.add_field(name="Coin system", value="<@695229647021015040> \n<@443769343138856961> \n<@713696771188195368>", inline=False)
        embed.add_field(name="Coin system help (ideas etc.)", value="<@761937966867152929>", inline=False)

        await ctx.respond(embed=embed)    


def setup(client):
    client.add_cog(credit(client))