import discord
from discord.ext import commands

class levels(commands.Cog):

    def __init__(self, client):
        self.client = client


    """@commands.command()
    async def levels(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/748122380383027210/883432420567834754/Levels.jpg")"""



    @commands.slash_command(name="levels_pcc1", description="Returns a picture with information about the levels in PCC1")
    async def levels_slash(self, ctx):
        await ctx.respond("https://cdn.discordapp.com/attachments/748122380383027210/883432420567834754/Levels.jpg")

def setup(client):
    client.add_cog(levels(client))        