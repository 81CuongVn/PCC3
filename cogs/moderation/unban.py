import discord
from discord.ext import commands

class unban(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="unban")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')
        for banned_entry in banned_users:
            user = banned_entry.user

            if(user.name, user.discriminator)==(member_name, member_disc):

                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {member_name}")
                return
        await ctx.send(f"Can't find {member}")  
        

def setup(client):
    client.add_cog(unban(client))