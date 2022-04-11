import discord
from discord.ext import commands
import asyncio
from discord.ext import tasks
from datetime import datetime
from datetime import date
import json
from discord.ext.commands import CommandNotFound
import os
from discord.utils import get
#from antispam import AntiSpamHandler, Options
from collections import Counter
import collections
import schedule
from discord.ext.commands import MemberNotFound
import sys
import subprocess
from decouple import config
# from AntiSpamTrackerSubclass import MyCustomTracker

other_log_channel=962765009006506024 #for main logging --> Default: 572673322891083776
spammers = []

class main_logger(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        @tasks.loop(seconds = 30) # repeat every 10 seconds
        async def myLoop():
            await asyncio.sleep(30)
            spammers.clear()

        myLoop.start()



    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot == True:
            return
        channel = self.client.get_channel(other_log_channel)
        embed = discord.Embed(description=f"**Message sent by {message.author.mention} deleted in <#{message.channel.id}>** \nContent: `{message.content}`", color=0xff0000, timestamp=datetime.now())  
        try:
            embed.set_author(name=f"{message.author.display_name}", icon_url=message.author.avatar.url) 
        except:
            embed.set_author(name=f"{message.author.display_name}")
        embed.set_footer(text=f"Author: {message.author.id} | Message ID: {message.id}") 
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        channel = self.client.get_channel(other_log_channel)
        if message_before.content == None or message_after.content == None:
            return
        else:
            embed = discord.Embed(description=f"**Message sent by {message_before.author.mention} edited in <#{message_before.channel.id}>**\n[Jump to message]({message_before.jump_url})", color=0x0037ff, timestamp=datetime.now())# \n\n**Before:** \n{message_before.content} \n\n**After:** \n{message_after.content}", color=0xff0000, timestamp=datetime.now())
            embed.add_field(name="Before", value=f"`{message_before.content}`", inline=False)
            embed.add_field(name="After", value=f"`{message_after.content}`", inline=False)  
            embed.set_author(name=f"{message_before.author.display_name}", icon_url=message_before.author.avatar.url) 
            embed.set_footer(text=f"Author: {message_before.author.id} | Message ID: {message_before.id}") 
            await channel.send(embed=embed) 

    @commands.Cog.listener()
    async def on_member_join(self, member):
        member_created = member.created_at.strftime("%m-%d-%Y")
        date_now = date.today()
        create_date = member.created_at.date()
        delta_create = date_now - create_date
        delta_create_int = int(delta_create.days)
        weeks = int(delta_create_int/7)
        months = int(delta_create_int/30.4375)
        years = int(delta_create_int/365)

        channel = self.client.get_channel(other_log_channel)
        embed = discord.Embed(description=f"{member.mention} {member}", color=0xff0000, timestamp=datetime.now())   
        embed.add_field(name="Account created at:", value=f"{member_created} MM-DD-YY") 
        embed.set_author(name=f"Member joined")
        embed.set_footer(text=f"{member.id}")
        try:
            embed.set_thumbnail(url=member.avatar.url)
        except:
            pass

        await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_member_leave(self, member):

        channel = self.client.get_channel(other_log_channel)
        embed = discord.Embed(description=f"{member.mention} {member}", color=0x1eff00, timestamp=datetime.now())   
        embed.set_author(name=f"Member left")
        embed.set_footer(text=f"{member.id}")
        try:
            embed.set_thumbnail(url=member.avatar.url)
        except:
            pass

        await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(main_logger(bot))