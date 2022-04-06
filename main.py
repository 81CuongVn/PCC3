
from tabnanny import check
import discord
from discord.ext import commands
import asyncio
from discord.ext import tasks
from discord.ext.commands import BucketType
from datetime import datetime
from datetime import timedelta
from datetime import date
import json
from discord.ext.commands import CommandNotFound
from discord.ui import Button, View
from discord import Option
from discord.ext.commands import MissingPermissions
import os
from discord.utils import get
#from antispam import AntiSpamHandler, Options
from collections import Counter
import collections
import schedule
from discord.ext.commands import MemberNotFound
import sys
import subprocess
# from AntiSpamTrackerSubclass import MyCustomTracker


#os.chdir("/home/pi/Desktop/PC_Creator_2")
client = commands.Bot(command_prefix=".", intents=discord.Intents.all(), case_insensitive=True)
client.remove_command('help')



@client.event
async def on_ready():
    print("Bot is online")
    await client.change_presence(activity=discord.Streaming(name="Playing PC Creator 2", url="https://www.youtube.com/watch?v=o9qoiH0Am7o"))
    client.start_time = datetime.now()

    @tasks.loop(seconds = 30) # repeat after every 10 seconds
    async def myLoop():
        await asyncio.sleep(30)
        spammers.clear() 
        #print(f"cleared at {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")
        #print(spammers)


    myLoop.start()

    #client.get_restriction = await get_restriction()
    #await new_restriction()


    while True:
        schedule.run_pending()
        await asyncio.sleep(1)  


spammers = []



@client.event
async def on_message(message):

    if not message.content.startswith(",") and not message.channel.id == 572673322891083776 and not message.channel.id == 748122380383027210 and not message.channel.id == 870068988254756894:    

            if isinstance(message.channel, discord.DMChannel):
                if message.author != client.user:
                    test_channel = client.get_channel(802512035224223774)
                    await test_channel.send(f'{message.author} sent "{message.content}" in DMs')
                return

            await new_member(message.author)

            user = message.author

            users = await get_messages()  

            messag_e = int(1)

            users[str(user.id)] += messag_e

            with open("userLevels.json", "w") as f:
                json.dump(users,f)  


            await new_coin_member(message.author)  

            user = message.author

            users_coins = await get_coins()  

            coins = int(1)

            users_coins[str(user.id)] += coins

            with open("usercoins.json", "w") as f:
                json.dump(users_coins,f)


            with open ("counter-file.txt", "r") as cf:
                data = cf.readlines()
                cf.close
            daily_messages = data[64]
            daily_messages_2 = int(daily_messages)
            test =  int(1)
            daily_messages_2 += test
            daily_messages_3 = str(daily_messages_2)
            data[64] = daily_messages_3
            with open ("counter-file.txt", "w") as cf:
                cf.writelines(data)
                cf.close     

    if message.author == client.user:
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
        test_channel = client.get_channel(933813622952562718)
        print(f"{message.author} wurde gebannt um {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}  -------> Informationen (Grund:Weirde Fehlfunktion): Spammer Liste:{spammers}")
        await test_channel.send(f"{message.author} wurde gebannt um {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}  -------> Informationen (Grund:Weirde Fehlfunktion): Spammer Liste:{spammers}")
        channel = client.get_channel(933768368970932254)
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

            

    await client.process_commands(message)  

@client.event
async def on_message_delete(message):
	#if message.author.bot:
		#return
    channel = client.get_channel(572673322891083776)
    embed = discord.Embed(description=f"**Message sent by {message.author.mention} deleted in <#{message.channel.id}>** \nContent: {message.content}", color=0xff0000, timestamp=datetime.now())  
    try:
        embed.set_author(name=f"{message.author.display_name}", icon_url=message.author.avatar.url) 
    except:
        embed.set_author(name=f"{message.author.display_name}")    
    embed.set_footer(text=f"Author: {message.author.id} | Message ID: {message.id}") 
    await channel.send(embed=embed)

@client.event
async def on_message_edit(message_before, message_after):    
    channel = client.get_channel(572673322891083776)
    try:
        if message_before.content == None or message_after.content == None:
            return
        embed = discord.Embed(description=f"**Message sent by {message_before.author.mention} edited in <#{message_before.channel.id}>** [Jump to message]({message_before.jump_url})", color=0x0037ff, timestamp=datetime.now())# \n\n**Before:** \n{message_before.content} \n\n**After:** \n{message_after.content}", color=0xff0000, timestamp=datetime.now())
        embed.add_field(name="Before", value=f"{message_before.content}", inline=False)
        embed.add_field(name="After", value=f"{message_after.content}", inline=False)  
        embed.set_author(name=f"{message_before.author.display_name}", icon_url=message_before.author.avatar.url) 
        embed.set_footer(text=f"Author: {message_before.author.id} | Message ID: {message_before.id}") 
        await channel.send(embed=embed)
    except:
        return    

@client.event
async def on_member_join(member):
    member_created = member.created_at.strftime("%m-%d-%Y")
    date_now = date.today()
    create_date = member.created_at.date()
    delta_create = date_now - create_date
    delta_create_int = int(delta_create.days)
    weeks = int(delta_create_int/7)
    months = int(delta_create_int/30.4375)
    years = int(delta_create_int/365)
    
    channel = client.get_channel(572673322891083776)
    embed = discord.Embed(description=f"{member.mention} {member}", color=0xff0000, timestamp=datetime.now())   
    embed.add_field(name="Account created at:", value=f"{member_created} MM-DD-YY") 
    embed.set_author(name=f"Member joined")
    embed.set_footer(text=f"{member.id}")
    try:
        embed.set_thumbnail(url=member.avatar.url)
    except:
        pass    
    
    await channel.send(embed=embed)


@client.event
async def on_member_leave(member):
    
    channel = client.get_channel(572673322891083776)
    embed = discord.Embed(description=f"{member.mention} {member}", color=0x1eff00, timestamp=datetime.now())   
    embed.set_author(name=f"Member left")
    embed.set_footer(text=f"{member.id}")
    try:
        embed.set_thumbnail(url=member.avatar.url)
    except:
        pass    
    
    await channel.send(embed=embed)
    

@client.command()
async def testo(ctx):
    await ctx.send(spammers)
    await ctx.send(collections.Counter(spammers))  


 


async def get_messages():
    with open("userLevels.json", "r") as f:
        users = json.load(f)
    return users   

async def new_member(user):

    users = await get_messages()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)] = 0        

    with open("userLevels.json", "w") as f:
        json.dump(users,f)
    return True         



async def get_coins():
    with open("usercoins.json", "r") as f:
        users_coins = json.load(f)
    return users_coins

async def new_coin_member(user):

    users_coins = await get_coins()

    if str(user.id) in users_coins:
        return False
    else:
        users_coins[str(user.id)] = {}
        users_coins[str(user.id)] = 0

    with open("usercoins.json", "w") as f:
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
#    for guild in client.guilds:
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



async def get_test():
    print("TEST")



@client.command(name="rsb")
async def rsb(ctx):
    if ctx.author.id == 443769343138856961 or ctx.author.id == 713696771188195368 or ctx.author.id == 695229647021015040:
        await ctx.send("Do you really want to do that? This can take up to 1 minute and could potentially break the bot. Reply with your user-ID to confirm.")
        ans = await client.wait_for('message', check=lambda message: message.author == ctx.author)
        print(ans.content)
        print(ctx.author.id)
        if int(ans.content) == int(ctx.author.id):
            await ctx.send("Restarting...")
            # os.system('restart.sh')
            # cmd = "C:\\Users\\zockerbande\\Desktop\\Neuer Ordner\\PC_Creator_2\\restart.sh"
            # os.execl('restart.sh', '')
            #os.execv(sys.executable, ['python'] + sys.argv)
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
        else:
            await ctx.send("Canceled")
    else:
        await ctx.send("HOW DARE YOU")




   

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)}')     


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return

    if isinstance(error, MemberNotFound):
        await ctx.send("Can't find this member")
        return
    raise error    

@client.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(error)
    else:
        raise error


initial_extensions = []
for directory in os.listdir('./cogs'):
    if directory != '__pycache__':
        for filename in os.listdir('./cogs/' + directory):
            #print(filename)
            if filename.endswith(".py"):
                if filename != 'importantfunctions.py':
                    initial_extensions.append("cogs." + directory + '.' + filename[:-3])
                    print(filename[:-3] + ' was loaded successfully')

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)    

client.run(os.environ['TOKEN_NYAN'])    