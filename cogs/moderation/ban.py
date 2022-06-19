import discord
from discord.ext import commands
import database.dbcon as db

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        rolelist = db.Server.Get.custom(str(ctx.guild.id), "MODERATION_ROLES")
        if not any(role.id in rolelist for role in ctx.author.roles):
            return False
        try:
            await ctx.message.delete()
        except:
            pass
        if  self.member_is_moderator(member):
            await ctx.send("You can't ban this member", delete_after=10)
            return False
        try:
            await member.ban(reason=reason)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " banned " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.ban(str(ctx.message.guild.id), str(member.id), str(reason))
            await member.send(f"You were banned on {ctx.message.guild.name} for {reason}")
            await ctx.send(f"Banned {member.mention}", delete_after=10)
        except:
            await member.ban(reason=reason)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " banned " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.ban(str(ctx.message.guild.id), str(member.id), str(reason))
            await ctx.send(f"Banned {member.mention}", delete_after=10)

    async def send_ban_message(self, ctx, member, reason):
        channel = self.client.get_channel(int(db.Server.Get.custom(str(ctx.guild.id), "mod-log-channel")))
        embed = discord.Embed(title="Banned", color=13565696)
        embed.add_field(name="Banned:", value=f"{member.mention}")
        embed.add_field(name="Moderator", value=f"{ctx.author.mention}")
        embed.add_field(name="Reason:", value=reason, inline=False)
        await channel.send(embed=embed)


def setup(client):
    client.add_cog(ban(client))