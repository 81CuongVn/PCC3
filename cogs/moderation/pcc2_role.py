import discord
from discord.ext import commands
import database.dbcon as db

class pcc2_role(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="pcc2r")
    async def pcc2role(self, ctx, member:discord.Member):
        rolelist = db.Server.Get.custom(str(ctx.guild.id), "PCC2_ROLES")
        user = ctx.author
        if any(role.id in rolelist for role in user.roles):
            await ctx.message.delete()
            role = ctx.guild.get_role(db.Server.Get.custom(str(ctx.guild.id), "PPR_ID"))
            await ctx.send(f"Added the **PCC2** role to **{member}**", delete_after=30)
            await member.add_roles(role)
        else:
            return


def setup(client):
    client.add_cog(pcc2_role(client))
