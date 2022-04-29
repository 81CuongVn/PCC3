import discord
from discord.ext import commands

class main(commands.Cog):

    def __init__(self, client):
        self.client = client


    """@commands.command()
    async def main(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/838857610358292532/912455051182755880/main.png")"""


    @commands.slash_command(name="main_screen_pcc1", description="Shows a picture of the main screen in game with information about the buttons")
    async def main_slash_pcc1(self, ctx):
        await ctx.respond("https://cdn.discordapp.com/attachments/838857610358292532/912455051182755880/main.png")    


def setup(client):
    client.add_cog(main(client))