import discord
from discord.ext import commands

class pcc2_role(commands.Cog):

    def __init__(self, client):
        self.client = client

 
    @commands.command(aliases=["pcc2r"])
    @commands.has_permissions(moderate_members = True)
    async def pcc2role(self, ctx, member:discord.Member):
        role = ctx.guild.get_role(934902778764091413)
        await ctx.send(f"Added role **PCC2** to **{member}**")
        await member.add_roles(role)


def setup(client):
    client.add_cog(pcc2_role(client)) 