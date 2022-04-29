import discord
from discord.ext import commands

class staff(commands.Cog):

    def __init__(self, client):
        self.client = client


    """@commands.command()
    async def staff(self, ctx):
        helper_role = discord.utils.get(ctx.channel.guild.roles, id=697728131003580537)
        botdev_role = discord.utils.get(ctx.channel.guild.roles, id=951207540472029195)
        embed = discord.Embed(title="Staff", color=13565696)
        embed.add_field(name="Administrator", value="<@387088097374109698>, \n<@695229647021015040>", inline=False)
        embed.add_field(name="Moderator", value="<@491620401810767881>, \n<@713696771188195368>", inline=False)
        embed.add_field(name="Trial-Mod", value="None", inline=False)
        embed.add_field(name="Helper", value=f"<@695229647021015040>, \n<@443769343138856961>, \n<@713696771188195368>, \n<@595176679006142465>, \n<@761937966867152929> \n\nIf you have a question with the game, you are open to ping or message a {helper_role.mention} to receive help.\n")
        embed.add_field(name="Bot Developer", value=f"<@695229647021015040>,\n<@443769343138856961>, \n<@713696771188195368>\n\nIf you encounter any problems with the <@884402383923339295>-Bot, feel free to report them to a {botdev_role.mention}")
        embed.set_footer(text="Some users are not displayed here because their activity on Discord is not moderation-oriented.")

        await ctx.send(embed=embed)"""


    @commands.slash_command(name="staff", description="Sends an embed with all staff members")
    async def staff_slash(self, ctx):
        helper_role = discord.utils.get(ctx.channel.guild.roles, id=697728131003580537)
        botdev_role = discord.utils.get(ctx.channel.guild.roles, id=951207540472029195)
        embed = discord.Embed(title="Staff", color=13565696)
        embed.add_field(name="Administrator", value="<@387088097374109698>, \n<@695229647021015040>", inline=False)
        embed.add_field(name="Moderator", value="<@491620401810767881>, \n<@713696771188195368>", inline=False)
        embed.add_field(name="Trial-Mod", value="None", inline=False)
        embed.add_field(name="Helper", value=f"<@695229647021015040>, \n<@443769343138856961>, \n<@713696771188195368>, \n<@595176679006142465>, \n<@761937966867152929> \n\nIf you have a question with the game, you are open to ping or message a {helper_role.mention} to receive help.\n")
        embed.add_field(name="Bot Developer", value=f"<@695229647021015040>,\n<@443769343138856961>, \n<@713696771188195368>\n\nIf you encounter any problems with the <@884402383923339295>-Bot, feel free to report them to a {botdev_role.mention}")
        embed.set_footer(text="Some users are not displayed here because their activity on Discord is not moderation-oriented.")

        await ctx.respond(embed=embed)


def setup(client):
    client.add_cog(staff(client))