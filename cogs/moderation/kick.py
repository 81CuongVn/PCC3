import discord
from discord.ext import commands
from discord.commands import permissions
import json
import database.dbcon as db

class kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="kick")
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        rolelist = db.Server.Get.custom(str(ctx.guild.id), "MODERATION_ROLES")
        if not any(role.id in rolelist for role in ctx.author.roles):
            return False
        try:
            await ctx.message.delete()
        except:
            pass
        if self.member_is_moderator(member):
            await ctx.send("You can't kick this member", delete_after=10)
            return False
        try:
            await member.kick(reason=reason)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " kicked " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.kick(str(ctx.message.guild.id), str(member.id), str(reason))
            await member.send(f"You were kicked from {ctx.message.guild.name} for {reason}")
            await ctx.send(f"Kicked {member.mention}", delete_after=10)
        except:
            await member.kick(reason=reason)
            db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " kicked " + str(member.id) + " for " + str(reason))
            db.Server.User.Add.kick(str(ctx.message.guild.id), str(member.id), str(reason))
            await ctx.send(f"Kicked {member.mention}", delete_after=10)
        await self.send_kick_message(ctx, member, reason)

    async def send_kick_message(self, ctx, member, reason):
        channel = self.client.get_channel(int(db.Server.Get.custom(str(ctx.guild.id), "mod-log-channel")))
        embed = discord.Embed(title="Kicked", color=13565696)
        embed.add_field(name="Kicked:", value=f"{member.mention}")
        embed.add_field(name="Moderator", value=f"{ctx.author.mention}")
        embed.add_field(name="Reason:", value=reason, inline=False)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(kick(client))