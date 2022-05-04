import discord
from discord.ext import commands
from discord import Option

rolelist = [589435378147262464, 648546626637398046, 632674518317531137, 571032502181822506]

class unban(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="unban", description="For Moderation")
    async def unban(self, ctx, *, member: Option(str, required = True)):
        user = ctx.author
        if any(role.id in rolelist for role in user.roles):
            await ctx.message.delete()
            banned_users = await ctx.guild.bans()
            member_name, member_disc = member.split('#')
            for banned_entry in banned_users:
                user = banned_entry.user

                if(user.name, user.discriminator)==(member_name, member_disc):

                    await ctx.guild.unban(user)
                    await ctx.send(f"Unbanned {member_name}", delete_after=10)
                    return
            await ctx.send(f"Can't find {member}", delete_after=10)
        else:
            return

def setup(client):
    client.add_cog(unban(client))