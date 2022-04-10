import discord
from discord.ext import commands
from discord import Option
import urllib
import re

class youtube(commands.Cog):

    def __init__(self, client):
        self.client = client



    
    @commands.command()
    async def youtube(self, ctx, *, search):
        searchwp = search.replace(" ", "+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchwp)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        print(video_ids[0])
        await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])

    @commands.slash_command(name="youtube", description="YouTube Video Search")
    async def youtube_slash(self, ctx, search: Option(str, required = True)):
        searchwp = search.replace(" ", "+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + searchwp)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        await ctx.respond("https://www.youtube.com/watch?v=" + video_ids[0])

def setup(client):
    client.add_cog(youtube(client))
