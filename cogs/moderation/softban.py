import discord
from discord.ext import commands
from discord.commands import permissions
import database.dbcon as db

class softban(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="softban")
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason = "No reason specified"):
        user = ctx.author
        rolelist = db.Server.Get.custom(str(ctx.guild.id), "MODERATION_ROLES")
        if any(role.id in rolelist for role in user.roles):
            await ctx.message.delete()
            if self.member_is_moderator(member):
                await ctx.send("You can't softban this member", delete_after=10)
                return False
            else:
                try:
                    await member.send(f"You were banned from the PC Creater server for:\n" + reason)
                    await member.ban(reason=reason)
                    await member.unban(reason=reason)
                    db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " kicked " + str(member.id) + " for " + str(reason))
                    db.Server.User.Add.kick(str(ctx.message.guild.id), str(member.id), str(reason))
                    await member.send(f"You were softbanned on {ctx.message.guild.name} for {reason}")
                    await ctx.send(f"Softbanned {member.mention}", delete_after=10)
                except:
                    await member.ban(reason=reason)
                    await member.unban(reason=reason)
                    db.Server.Add.action(str(ctx.guild.id), str(ctx.message.author.id) + " kicked " + str(member.id) + " for " + str(reason))
                    db.Server.User.Add.kick(str(ctx.message.guild.id), str(member.id), str(reason))
                    await member.send(f"You were softbanned on {ctx.message.guild.name} for {reason}")
                    await ctx.send(f"Softbanned {member.mention}", delete_after=10)
                await self.send_softban_message(ctx, member, reason)
        else:
            return

    async def send_softban_message(self, ctx, member, reason):
        channel = self.client.get_channel(int(db.Server.Get.custom(str(ctx.guild.id), "mod-log-channel")))
        embed = discord.Embed(title="Softbanned", color=13565696)
        embed.add_field(name="Softbanned:", value=f"{member.mention}")
        embed.add_field(name="Moderator", value=f"{ctx.author.mention}")
        embed.add_field(name="Reason:", value=reason, inline=False)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(softban(client))