import discord
from discord.ext import commands

class bitcoinpc(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="bitcoinpc", aliases=["miner", "bitcoinminer", "btcpc"])
    async def bitcoinpc(self, ctx):
        await ctx.send("https://media.discordapp.net/attachments/802512035224223774/948613438295408690/Bitcoin_PC_4.jpg")


    @commands.slash_command(name="miner_pcc1", description="Shows a chart with good mining setups for every level")
    async def bitcoinpc_slash_pcc1(self, ctx):
        await ctx.respond("https://media.discordapp.net/attachments/802512035224223774/948613438295408690/Bitcoin_PC_4.jpg")    


def setup(client):
    client.add_cog(bitcoinpc(client))