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
        embed=discord.Embed(title="Update 1.10", description="What is new?", color=13565696)
        embed.set_author(name=f"{ctx.author.name}", url=f"https://discordapp.com/users/{ctx.author.id}", icon_url=f"{ctx.author.avatar.url}")
        embed.add_field(name="Levelsystem", value="We changed our level system to XP. <:pog:813886729235988541>\nYou should get your XP in the next few hours.", inline=False)
        embed.add_field(name="Trading", value="You can now trade with other users using `/trading`. You can use `/check_trades` or `,checktrades` to check for available trades.", inline=False)
        embed.add_field(name="Items", value="We have added new items (games) to the shop.", inline=False)
        embed.add_field(name="Bug fixes", value="We fixed a few bugs, again. This probably has a few bugs due to the new features. So feel free to report any bugs to a Bot Developer, so they can work on fixing it soon.", inline=False)
        embed.set_footer(text="Stay tuned for the next update. 😉")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(botnews_command(client))