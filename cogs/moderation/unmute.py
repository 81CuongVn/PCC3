import discord
from discord.ext import commands
from discord import Option
from discord.ext.commands import MissingPermissions
from discord.commands import permissions

rolelist = [589435378147262464, 648546626637398046, 632674518317531137, 571032502181822506, 697002610892341298]

class unmute(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name = 'unmute')
    async def unmute(self, ctx, member: Option(discord.Member, required = True), reason: Option(str, required = False)):
        user = ctx.author
        if any(role.id in rolelist for role in user.roles):
            await ctx.message.delete()
            if reason == None:
                await member.remove_timeout()
                await ctx.respond(f"<@{member.id}> has been untimed out by <@{ctx.author.id}>.", delete_after=10)
            else:
                await member.remove_timeout(reason = reason)
                await ctx.respond(f"<@{member.id}> has been untimed out by <@{ctx.author.id}> for '{reason}'.", delete_after=10)
        else:
            return

    @unmute.error
    async def unmuteerror(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("You can't do this! You need to have moderate members permissions!", delete_after=10)
        else:
            raise error


def setup(client):
    client.add_cog(unmute(client))