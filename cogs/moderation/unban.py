import discord
from discord.ext import commands
from discord import Option

class unban(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="unban", description="For Moderation")
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, *, member: Option(str, required = True)):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')
        for banned_entry in banned_users:
            user = banned_entry.user

            if(user.name, user.discriminator)==(member_name, member_disc):

                await ctx.guild.unban(user)
                await ctx.respond(f"Unbanned {member_name}")
                return
        await ctx.respond(f"Can't find {member}")
        

def setup(client):
    client.add_cog(unban(client))