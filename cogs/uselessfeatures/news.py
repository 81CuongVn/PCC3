import discord
from discord.ext import commands
from discord.commands import permissions

class botnews_command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="botnews")
    @permissions.has_any_role(951207540472029195, 951464246506565683)
    async def botnews(self, ctx):
        await ctx.message.delete()
        embed=discord.Embed(title="Update 1.9", description="What is new?", color=13565696)
        embed.set_author(name="Yui", url="https://discordapp.com/users/443769343138856961", icon_url="https://cdn.discordapp.com/avatars/443769343138856961/a_0d00fcc52d83500cc2915ff9f19d877d.gif?size=1024")
        embed.add_field(name="Tic Tac Toe", value="We finally updated Tic Tac Toe to v2.\nYou can play with `/tic_tac_toe`", inline=False)
        embed.add_field(name="Notes", value="We added a `,note` command, so you can finally remember all the things you always forget.", inline=False)
        embed.add_field(name="Bug fixes", value="We fixed many bugs, and made sure, that this release is mostly \"bug free\".", inline=False)
        embed.set_footer(text="Stay tuned for the next update. 😉")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(botnews_command(client))