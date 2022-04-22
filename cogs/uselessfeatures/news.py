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
        embed=discord.Embed(title="Update 1.9.1", description="What is new?", color=13565696)
        embed.set_author(name=f"{ctx.author.name}", url=f"https://discordapp.com/users/{ctx.author.id}", icon_url=f"{ctx.author.avatar.url}")
        embed.add_field(name="FAQ", value="We decided to add a FAQ-System so that we can answer your PCC dedicated questions. <:pog:813886729235988541>\nTo use it, just type `,faq_ask` or `/faq_ask`", inline=False)
        embed.add_field(name="Bug fixes", value="We fixed no bugs... ¯\\\\\_(ツ)\\_\\/¯ But we made sure, that this release is mostly \"bug free\" again.", inline=False)
        embed.set_footer(text="Stay tuned for the next update. 😉")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(botnews_command(client))