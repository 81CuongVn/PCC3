from http import server
from xmlrpc.client import Server
import discord
from discord.ext import commands
from datetime import datetime
import json
from discord.utils import get
from discord.ext import tasks
from discord import Option
import random
from discord.commands import permissions


class messagecoins(commands.Cog):

    def __init__(self, client):
        self.client = client

    



    async def bal(self, ctx, send, member):
        await self.new_member(ctx.author)
        user = member
        users_coins = await self.get_coins()
        messages_amt_str = users_coins[str(user.id)]
        messages_amt = int(messages_amt_str)
        embed = discord.Embed(title=f"{member.display_name}'s Money", color=ctx.author.colour)
        embed.add_field(name="Coins:", value=f"{messages_amt}<:bot_icon:951868023503986699>")
        try:
            embed.set_thumbnail(url=member.avatar.url)
        except:
            pass
        await send(embed=embed)


    async def get_coins(self):
        with open("json_files/usercoins.json", "r") as f:
            users_coins = json.load(f)
        return users_coins

    async def new_member(self, user):

        users_coins = await self.get_coins()

        if str(user.id) in users_coins:
            return False
        else:
            users_coins[str(user.id)] = {}
            users_coins[str(user.id)] = 0

        with open("json_files/usercoins.json", "w") as f:
            json.dump(users_coins,f)
        return True




  

    async def lead(self, send, url):
        with open("json_files/usercoins.json", "r") as f:
            data = json.load(f)

            leaderboard = sorted(data.items(), key= lambda x: x[1], reverse=True)[:5]
            embed= discord.Embed(title="Bank", color=13565696)
            if len(leaderboard) >= 5:
                user_id_1st, msg_count_1st = leaderboard[0]
                user_id_2nd, msg_count_2nd = leaderboard[1]
                user_id_3rd, msg_count_3rd = leaderboard[2]
                user_id_4th, msg_count_4th = leaderboard[3]
                user_id_5th, msg_count_5th = leaderboard[4]
                embed.add_field(name="Richest users", value=f"`1.` <@{user_id_1st}>: {msg_count_1st}<:bot_icon:951868023503986699> \n`2.` <@{user_id_2nd}>: {msg_count_2nd}<:bot_icon:951868023503986699> \n`3.` <@{user_id_3rd}>: {msg_count_3rd}<:bot_icon:951868023503986699> \n`4.` <@{user_id_4th}>: {msg_count_4th}<:bot_icon:951868023503986699> \n`5.` <@{user_id_5th}>: {msg_count_5th}<:bot_icon:951868023503986699>")
            else:
                embed.add_field(name="How can you see this?", value="There have been less than 5 people sending a message since the data was reset")
            try:
                embed.set_thumbnail(url=url)
            except:
                pass
            await send(embed=embed)

    


    


    

def setup(client):
    client.add_cog(messagecoins(client))