import discord
from discord.ext import commands
from discord.commands import permissions
import json
from discord.ui import Button, View

class leave(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="leave", description="Just leave the server")
    async def leave(self, ctx):
        
        member = ctx.author

        await ctx.respond(f"{member.mention} do you really want to leave? Answer with `y/n`")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel 
    
        msg = await self.client.wait_for('message', check=check)  

        if msg.content.lower() == "y" or msg.content.lower() == "yes":
            await ctx.send(f"{member.mention} left the server")
            await member.kick(reason="Used leave command")
        if msg.content.lower() == "n" or msg.content.lower() == "no":
            await ctx.send("Ok you want to stay. Thats cool")    
        else:
            await ctx.send(f"You have to answer with y/n. Please use /leave again") 

        

def setup(client):
    client.add_cog(leave(client))