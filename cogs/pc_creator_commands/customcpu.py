import discord
from discord.ext import commands

class customcpu(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="CustomCpu")
    async def customcpu(self, ctx):
        embed = discord.Embed(title="~~This is how custom CPUs where made~~", color=13565696)
        embed.set_image(url="https://images-ext-2.discordapp.net/external/uADQCXXNQ6xx3QHW8_cPLJ8w0kGUg1oiQDmxSVAvjGQ/https/media.discordapp.net/attachments/571031705109135361/809885303119675482/Screenshot_2021-02-12-17-34-34-411_com.ultraandre.pccreator.jpg?width=930&height=441")
        embed.set_footer(text="You cannot make custom CPUs anymore. The feature to manufacture them was removed in an update")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(customcpu(client))