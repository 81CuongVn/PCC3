import discord
from discord.ext import commands
from discord import Option
import requests
from bs4 import BeautifulSoup

headers = {
	        'Accept' : '*/*',
	        'Accept-Language': 'en-US,en;q=0.5',
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
}

class google(commands.Cog):

    def __init__(self, client):
        self.client = client

    """@commands.command()
    async def google(self, ctx, *, search=None):
        if search == None:
            search = "google"
        url = 'https://www.google.com/search'
        parameters = {'q': search}
        content = requests.get(url, headers = headers, params = parameters).text
        soup = BeautifulSoup(content, 'html.parser')
        search = soup.find(id = 'search')
        first_link = search.find('a')
        await ctx.send(first_link['href'])"""

    @commands.slash_command(name="google", description="Google Search")
    async def google_slash(self, ctx, search: Option(str, required = True)):
        url = 'https://www.google.com/search'
        parameters = {'q': search}
        content = requests.get(url, headers = headers, params = parameters).text
        soup = BeautifulSoup(content, 'html.parser')
        search = soup.find(id = 'search')
        first_link = search.find('a')
        await ctx.respond(first_link['href'])


def setup(client):
    client.add_cog(google(client))
