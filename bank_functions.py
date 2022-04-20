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
import hashlib
import os
import uuid
import numpy as np
import binascii

class jsonEncoding(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)

async def get_bank_data():
        with open("json_files/bank.json", "r") as f:
            bank_account = json.load(f)
        return bank_account

async def check_for_bank_account(ctx, send, member):

    user = member

    bank_account = await get_bank_data()

    if str(user.id) in bank_account:
        return False  
    else:
        await send("Use /create_bank_account to create a bank account", ephemeral=True)
        return

async def new_bank_account(self, ctx, send, member, password):
        user = member
        bank_account = await get_bank_data()
        password = await hash_password(password)
        if str(user.id) in bank_account:
            return "You already have a bank account, to reset your Password use `/reset_bank_password`"
        else:  
          
            bank_account[str(user.id)] = {}
            bank_account[str(user.id)]["money"] = 0
            bank_account[str(user.id)]["password"] = password.decode("utf-8")

        file = open('json_files/bank.json', 'w', encoding='utf-8');
        file.write(json.dumps(bank_account, indent=4))
        file.close()
        #with open("json_files/bank.json", "w") as f:
        #    json.dump(bank_account,f)
        return "Successfully created your bank account. If you forget your password, use `/reset_bank_password`"


async def update_bank(member, send, amount, mode):

    try:
        user = member.id
    except:
        user = member

    bank_account = await get_bank_data()
    users_coins = await get_coins()

    if mode == "bank":
        bank_money_amount = bank_account[str(user)]["money"]

        if amount <= 0:
            if amount > bank_money_amount:
                await send("You dont have enough money")
                return
        
        bank_account[str(user)] += amount  
        with open("json_files/bank.json", "w") as f:
            json.dump(bank_account,f)
          
    elif mode == "wallet":
        wallet_money_amount = users_coins[str(user)]

        if amount <= 0:
            if amount > wallet_money_amount:
                await send("You dont have enough money")
                return
        
        users_coins[str(user)] += amount
        with open("json_files/usercoins.json", "w") as f:
            json.dump(users_coins,f)

        
         
async def get_coins():
        with open("json_files/usercoins.json", "r") as f:
            users_coins = json.load(f)
        return users_coins

async def change_coins(ctx, member, amount, subtract):
    user = member
    bank_account = await get_bank_data()
    if str(user.id) not in bank_account:
        print("OK")
    messages_amt_str = bank_account[str(user.id)]["money"]
    messages_amt = int(messages_amt_str)
    bank_account[str(user.id)]["money"] += -1*messages_amt
    if subtract == False:
        coinamount = amount + messages_amt
    elif subtract == True:
        coinamount = messages_amt - amount
    bank_account[str(user.id)]["money"] = coinamount
    with open("json_files/bank.json", "w") as f:
        json.dump(bank_account,f)
    return True
    

async def bal(ctx, member):
    await new_member(ctx.author)
    user = member
    users_coins = await get_coins()
    if str(user.id) not in users_coins:
        await new_member(user)
    messages_amt_str = users_coins[str(user.id)]
    messages_amt = int(messages_amt_str)
    return messages_amt 


async def bank_bal(ctx, user):
    member = user
    send = ctx.respond
    await check_for_bank_account(ctx, send, member)
    bank_account = await get_bank_data()
    if str(user.id) not in bank_account:
        await ctx.respond("Use `/create_bank_account` to create a bank account", ephemeral=True)
        return
    messages_amt_str = bank_account[str(user.id)]["money"]
    messages_amt = int(messages_amt_str)
    return messages_amt   

async def new_member(user):

    users_coins = await get_coins()

    if str(user.id) in users_coins:
        return False
    else:
        users_coins[str(user.id)] = {}
        users_coins[str(user.id)] = 0

    with open("json_files/usercoins.json", "w") as f:
        json.dump(users_coins,f)
    return True

async def balance_command(ctx, send, member):
    await new_member(member)
    user = member
    users_coins = await get_coins()
    coins_amt_str = users_coins[str(user.id)]
    coins_amt = int(coins_amt_str)
    bank_stuff = await get_bank_data()
    try:
        coins_bank_amt_str = bank_stuff[str(user.id)]["money"]
    except:
        coins_bank_amt_str = 0
    bank_coins = int(coins_bank_amt_str)
    coins_bank_amt = int(bank_coins)
    embed = discord.Embed(title=f"{member.display_name}'s Money", color=ctx.author.colour)
    embed.add_field(name="Coins:", value=f"{coins_amt}<:bot_icon:951868023503986699>")
    embed.add_field(name="Bank:", value=f"{coins_bank_amt}<:bot_icon:951868023503986699>")
    try:
        embed.set_thumbnail(url=member.avatar.url)
    except:
        pass
    await send(embed=embed)   


async def lead(send, url):
    with open("json_files/usercoins.json", "r") as w:
        wallet = json.load(w)
    with open("json_files/bank.json", "r") as b:
        bank = json.load(b)
    wallet = sorted(wallet.items(), key= lambda x: x[1], reverse=True)[:5]
    bank = sorted(bank.items(), key= lambda x: x[1].get('money', 0), reverse=True)[:5]
    embed = discord.Embed(title="Bank", color=13565696, type="rich")
    if len(wallet) >= 5 and len(bank) >= 5:
        user_id_1st_wallet, msg_count_1st_wallet = wallet[0]
        user_id_2nd_wallet, msg_count_2nd_wallet = wallet[1]
        user_id_3rd_wallet, msg_count_3rd_wallet = wallet[2]
        user_id_4th_wallet, msg_count_4th_wallet = wallet[3]
        user_id_5th_wallet, msg_count_5th_wallet = wallet[4]

        msg_count_1st_bank = bank[0][1]['money']
        msg_count_2nd_bank = bank[1][1]['money']
        msg_count_3rd_bank = bank[2][1]['money']
        msg_count_4th_bank = bank[3][1]['money']
        msg_count_5th_bank = bank[4][1]['money']

        user_id_1st_bank = bank[0][0]
        user_id_2nd_bank = bank[1][0]
        user_id_3rd_bank = bank[2][0]
        user_id_4th_bank = bank[3][0]
        user_id_5th_bank = bank[4][0]

        with open("json_files/usercoins.json", "r") as w:
            coinsystem = json.load(w)
        with open("json_files/bank.json", "r") as b:
            banksystem = json.load(b)

        richarray = []
        richarraynum = 0
        for user in coinsystem:
            if user in banksystem:
                user_money = coinsystem[user] + banksystem[user]['money']
                richarray.append([])
                richarray[richarraynum].append(user)
                richarray[richarraynum].append(user_money)
                richarraynum += 1

        #print(richarray)

        embed.add_field(name="Biggest wallets\t", value=f"`1.` <@{user_id_1st_wallet}>: {msg_count_1st_wallet}<:bot_icon:951868023503986699> \n`2.` <@{user_id_2nd_wallet}>: {msg_count_2nd_wallet}<:bot_icon:951868023503986699> \n`3.` <@{user_id_3rd_wallet}>: {msg_count_3rd_wallet}<:bot_icon:951868023503986699> \n`4.` <@{user_id_4th_wallet}>: {msg_count_4th_wallet}<:bot_icon:951868023503986699> \n`5.` <@{user_id_5th_wallet}>: {msg_count_5th_wallet}<:bot_icon:951868023503986699>")
        
        embed.add_field(name="Biggest bank accounts\t", value=f"`1.` <@{user_id_1st_bank}>: {msg_count_1st_bank}<:bot_icon:951868023503986699> \n`2.` <@{user_id_2nd_bank}>: {msg_count_2nd_bank}<:bot_icon:951868023503986699> \n`3.` <@{user_id_3rd_bank}>: {msg_count_3rd_bank}<:bot_icon:951868023503986699> \n`4.` <@{user_id_4th_bank}>: {msg_count_4th_bank}<:bot_icon:951868023503986699> \n`5.` <@{user_id_5th_bank}>: {msg_count_5th_bank}<:bot_icon:951868023503986699>")

        if richarraynum >= 4:
            richarray.sort(key= lambda x: x[1], reverse=True)
            embed.add_field(name="Richest users\t", value=f"`1.` <@{richarray[0][0]}>: {richarray[0][1]}<:bot_icon:951868023503986699> \n`2.` <@{richarray[1][0]}>: {richarray[1][1]}<:bot_icon:951868023503986699> \n`3.` <@{richarray[2][0]}>: {richarray[2][1]}<:bot_icon:951868023503986699> \n`4.` <@{richarray[3][0]}>: {richarray[3][1]}<:bot_icon:951868023503986699> \n`5.` <@{richarray[4][0]}>: {richarray[4][1]}<:bot_icon:951868023503986699>", inline=False)
        else:
            embed.add_field(name="Richest users\t", value=f"There are less than 5 users having a bank account and a wallet.\nIf you can see this, please contact a Bot Developer", inline=False)
    else:
         embed.add_field(name="How can you see this?", value="There have been less than 5 people sending a message and depositing money into their bank since the data was last reset.")
    try:
        embed.set_thumbnail(url=url)
    except:
        pass
    await send(embed=embed)  


async def get_useritems():
    with open("json_files/useritems.json", "r") as f:
        users_items = json.load(f)
    return users_items  


async def hash_password(password):
    salt = hashlib.sha256(os.urandom(64)).hexdigest().encode('ascii')
    #print(salt)
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    pwdhash = salt + pwdhash
    #print(pwdhash)
    return pwdhash

async def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    salt = salt.encode('ascii')
    #print(salt)
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    #print(pwdhash)
    stored_password = "b'" + stored_password + "'"
    #print(stored_password)
    if str(pwdhash) == str(stored_password):
        return 'yes'
    else:
        return 'no'


async def set_things(member, mode, mode_2, amount):
    if mode == "wallet":
        await new_member(member)
        users_coins = await get_coins()
        if mode_2 == "set":
            content = f"Set {member}'s <:bot_icon:951868023503986699> to {amount} (mode: wallet)"
            users_coins[str(member.id)] = amount
        if mode_2 == "give":
            content = f"Gave {member} {amount}<:bot_icon:951868023503986699> (mode: wallet)"
            users_coins[str(member.id)] += amount
        with open("json_files/usercoins.json", "w") as f:
            json.dump(users_coins,f)
        return content
    if mode == "bank":
        bank_account = await get_bank_data()
        if not str(member.id) in bank_account:
            content = "No bank account found"
            return content
        else:  
            if mode_2 == "set":
                content = f"Set {member}'s bank <:bot_icon:951868023503986699> to {amount} (mode: bank)"
                bank_account[str(member.id)]["money"] = amount
            if mode_2 == "give":
                content = f"Gave {member} {amount}<:bot_icon:951868023503986699> (mode: bank)"
                bank_account[str(member.id)]["money"] += amount
            with open("json_files/bank.json", "w") as f:
                json.dump(bank_account,f)
            return content
    if mode == "messages":
        users = await get_messages()
        await new_message_member(member)
        if mode_2 == "set":
            content = f"Set {member}'s messages to {amount} (mode: messages)"
            users[str(member.id)] = amount
        if mode_2 == "give":
            content = f"Gave {member} {amount} messages (mode: messages)"
            users[str(member.id)] += amount
        with open("json_files/userLevels.json", "w") as f:
            json.dump(users,f)
        return content  



async def get_messages():
    with open("json_files/userLevels.json", "r") as f:
        users = json.load(f)
    return users   

async def new_message_member(user):

    users = await get_messages()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)] = 0        

    with open("json_files/userLevels.json", "w") as f:
        json.dump(users,f)
    return True   
                


async def get_trading_list():
    with open("json_files/trading_list.json", "r") as f:
        trading_list = json.load(f)
    return trading_list
    
async def get_trading():
    with open("json_files/trading_member.json", "r") as f:
        trading = json.load(f)
    return trading

async def new_trading_member(member):
    trading = await get_trading()

    if str(member.id) in trading:
        return False
    else:
        trading[str(member.id)] = []

    with open("json_files/trading_member.json", "w") as f:
        json.dump(trading,f)
    return True    
                
