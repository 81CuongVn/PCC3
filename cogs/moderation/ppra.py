import discord
from discord.ext import commands
from discord.commands import permissions
from discord import Option

rolelist = [589435378147262464, 632674518317531137]

class ppra(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="ppra")
    async def ppra(self, ctx, member: Option(discord.Member, required = True)):
        user = ctx.author
        if any(role.id in rolelist for role in user.roles):
            await ctx.message.delete()
            role = ctx.guild.get_role(775736993018806322)
            await ctx.send(f"Added role **PRO PLAYER** to **{member}**")
            await member.add_roles(role) 
        else:
            return


def setup(client):
    client.add_cog(ppra(client)) 