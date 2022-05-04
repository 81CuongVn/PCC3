import discord
from discord.ext import commands
from discord import Option
from discord.ext.commands import MissingPermissions
from discord.commands import permissions

rolelist = [589435378147262464, 648546626637398046, 632674518317531137, 571032502181822506, 697002610892341298, 951464246506565683]

class unmute(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="unmute")
    async def unmute(self, ctx, member: discord.Member):
        user = ctx.author
        if any(role.id in rolelist for role in user.roles):
            await ctx.message.delete()
            if True:
                await member.remove_timeout()
                await ctx.send(f"<@{member.id}> has been untimed out by <@{ctx.author.id}>", delete_after=10)
        else:
            return

    @unmute.error
    async def unmuteerror(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You can't do this! You need to have moderate members permissions!", delete_after=10)
        else:
            raise error


def setup(client):
    client.add_cog(unmute(client))