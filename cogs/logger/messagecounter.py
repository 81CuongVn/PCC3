﻿import discord
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

test_channel=933813622952562718 #only mentioned once --> Default: 933813622952562718
channel_channel=933768368970932254 #only mentioned once --> Default: 933768368970932254
message_channel=802512035224223774 #for on_message --> Default: 802512035224223774
other_log_channel=572673322891083776 #for main logging --> Default: 572673322891083776
spammers = []

class messagecounter(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_message(self, message):
        if True:
            if not message.content.startswith(",") and not message.channel.id == other_log_channel and not message.channel.id == 748122380383027210 and not message.channel.id == 870068988254756894:    
                    if isinstance(message.channel, discord.DMChannel):
                        if message.author != self.client.user:
                            test_channel = self.client.get_channel(message_channel)
                            await test_channel.send(f'{message.author} sent "{message.content}" in DMs')
                        return
                    await self.new_member(message.author)
                    user = message.author
                    users = await self.get_messages()  
                    messag_e = int(1)
                    users[str(user.id)] += messag_e
                    with open("json_files/userLevels.json", "w") as f:
                        json.dump(users,f)  
                    await self.new_coin_member(message.author)
                    user = message.author
                    users_coins = await self.get_coins()
                    coins = int(1)
                    users_coins[str(user.id)] += coins
                    with open("json_files/usercoins.json", "w") as f:
                        json.dump(users_coins,f)
                    with open ("json_files/counter-file.txt", "r") as cf:
                        data = cf.readlines()
                        cf.close
                    daily_messages = data[64]
                    daily_messages_2 = int(daily_messages)
                    test = int(1)
                    daily_messages_2 += test
                    daily_messages_3 = str(daily_messages_2)
                    data[64] = daily_messages_3
                    with open ("counter-file.txt", "w") as cf:
                        cf.writelines(data)
                        cf.close
            if message.author == self.client.user:
                return
            filtered_words = []#["fuck", "idiot", "shit", "fuck", "nigg", "fuk", "cunt", "cnut", "bitch", "dick", "d1ck", "pussy,", "asshole", "b1tch", "b!tch", "blowjob", "cock", "c0ck", "f u c k", "shlt", "fů", "cum", "shit" "ass", "fuc", "nigg", "fuk", "cunt", "cnut", "bitch", "dick",  "d1ck", "pussy", "asshole", "b1tch", "b!tch", "blowjob", "cock", "c0ck", "retard", "fag", "faggot"]
            topleveldomain = ["https://", "http://"] #"com", "org", "net"]
            #for word in topleveldomain:
            #     if word in message.content:
            #         print("Domain True")
            #if "@everyone" in message.content:
            #     print("Everyone True")        
            #if len(message.content) > 32:
            #     print("Größer 32")
            for word in topleveldomain:
                #and ("@everyone" in message.content or "@here" in message.content or "everyone" in message.content or "here" in message.content))
                if word in message.content and len(message.content) > 32 and not (".jpg" in message.content or ".png" in message.content):
                    spammers.append(message.author.id)   
            if Counter(spammers)[message.author.id] >= 3:
                await message.channel.send(f"{message.author.mention} stop spamming that message. If you continue spamming, you will be **banned**. In case there are problems and you are not a scamer, send a DM to ¥£$#7660 (695229647021015040)", delete_after=10)       
            if Counter(spammers)[message.author.id] >= 4:
                test_channel = self.client.get_channel(test_channel)
                print(f"{message.author} wurde gebannt um {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}  -------> Informationen (Grund:Weirde Fehlfunktion): Spammer Liste:{spammers}")
                await test_channel.send(f"{message.author} wurde gebannt um {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}  -------> Informationen (Grund:Weirde Fehlfunktion): Spammer Liste:{spammers}")
                channel = self.client.get_channel(channel_channel)
                try:
                    await message.author.send(f"You were softbanned on the PC Creater server. In case you think this was a mistake from the bot, send a message to ¥£$#7660 (695229647021015040)")
                    await message.author.send(f"reason: Scam")
                except:
                    return
                embed = discord.Embed(title="Softbanned", color=13565696)
                embed.add_field(name="Softbanned:", value=f"{message.author.mention}")
                embed.add_field(name="Moderator", value=f"<@884402383923339295>")
                embed.add_field(name="Reason:", value="Scam", inline=False)
                await channel.send(embed=embed)    
                await message.channel.send(f"Softbanned {message.author.mention}", delete_after=10)
                await message.author.ban(reason="Scam")  
                await message.author.unban(reason="Scam")    
            member = message.author
            for word in filtered_words:
                if word in message.content.lower() and not get(member.roles, id=589435378147262464) and not get(member.roles, id=934116557951475783) and not get(member.roles, id=659740600911921153):
                    await message.delete()
                    await message.channel.send("This word is banned here" ,delete_after=5.0)
                    break
            if message.channel.id == 572541644755435520:
                if not message.content.startswith(",suggest"):
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} Please use the **,suggest** command to suggest things here", delete_after=10)   
            if message.channel.id == 940691696918880326:
                await message.delete()                 
                await message.channel.send(f"{message.author.mention} Please use the **/suggest_pcc2** command to suggest things", delete_after=10)     
            #await self.client.process_commands(message) WEHE JEMAND AUSKOMMENTIERT DAS!!! ICH ZERMATSCHE DICH!!! DAS HERAUSZUFINDEN DASS MAN DAS AUSKOMMENTIEREN MUSS HAT MICH 3 STUNDEN GEKOSTET!!!!!!!!!!!!!!

    async def get_messages(self):
        with open("json_files/userLevels.json", "r") as f:
            users = json.load(f)
        return users   

    async def new_member(self, user):

        users = await self.get_messages()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)] = 0        

        with open("json_files/userLevels.json", "w") as f:
            json.dump(users,f)
        return True         



    async def get_coins(self):
        with open("json_files/usercoins.json", "r") as f:
            users_coins = json.load(f)
        return users_coins

    async def new_coin_member(self, user):

        users_coins = await self.get_coins()

        if str(user.id) in users_coins:
            return False
        else:
            users_coins[str(user.id)] = {}
            users_coins[str(user.id)] = 0

        with open("json_files/usercoins.json", "w") as f:
            json.dump(users_coins,f)
        return True

    #async def get_restriction():
    #    with open("channel_restrictions.json", "r") as f:
    #        restriction = json.load(f)
    #    return restriction
    #
    #async def check_restriction(ctx):
    #    restriction = await get_restriction()
    #    
    #    if restriction[str(ctx.channel.id)]["Server"] == 1:
    #        await ctx.send("This command is restricted. You can use it in the #bot-commands channel")
    #
    #async def new_restriction():
    #
    #    for guild in self.client.guilds:
    #        for channel in guild.channels:
    #            print(channel.id, channel.name)
    #
    #            restriction = await get_restriction()
    #
    #            if str(channel.id) in restriction:
    #                pass
    #            else:
    #                restriction[str(channel.id)] = {}
    #                restriction[str(channel.id)]["Moderation"] = 0
    #                restriction[str(channel.id)]["Scores"] = 0
    #                restriction[str(channel.id)]["PCC_Content"] = 0
    #                restriction[str(channel.id)]["Server"] = 0  
    #
    #            with open("channel_restrictions.json", "w") as f:
    #                json.dump(restriction,f)
    #            #return True        



    async def get_test(self):
        print("TEST")

def setup(bot):
    bot.add_cog(messagecounter(bot))