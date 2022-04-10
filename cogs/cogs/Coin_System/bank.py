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


class jsonEncoding(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)

class banktransfer(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def get_coins(self):
            with open("usercoins.json", "r") as f:
                users_coins = json.load(f)
            return users_coins

    async def change_coins(self, ctx, member, amount, subtract):
        user = member
        users_coins = await self.get_coins()
        if str(user.id) not in users_coins:
            await self.new_member(user)
        messages_amt_str = users_coins[str(user.id)]
        messages_amt = int(messages_amt_str)
        users_coins[str(user.id)] += -1*messages_amt
        if subtract == False:
            coinamount = amount + messages_amt
        elif subtract == True:
            coinamount = messages_amt - amount
        users_coins[str(user.id)] = coinamount
        with open("usercoins.json", "w") as f:
            json.dump(users_coins,f)
        return True
        
    
    async def bal(self, ctx, member):
        await self.new_member(ctx.author)
        user = member
        users_coins = await self.get_coins()
        if str(user.id) not in users_coins:
            await self.new_member(user)
        messages_amt_str = users_coins[str(user.id)]
        messages_amt = int(messages_amt_str)
        return messages_amt

    async def new_member(self, user):

        users_coins = await self.get_coins()

        if str(user.id) in users_coins:
            return False
        else:
            users_coins[str(user.id)] = {}
            users_coins[str(user.id)] = 0

        with open("usercoins.json", "w") as f:
            json.dump(users_coins,f)
        return True


    


    """@commands.slash_command(name="create_bank_account", description="Create a bank account to deposit and withdraw your coins")
    async def create_bank_account_slash(self, ctx, password: Option(str, required=True)):
        member = ctx.author
        send = ctx.respond
        await self.new_bank_account(ctx, send, member, password)
  """


    async def get_bank_data(self):
            with open("bank.json", "r") as f:
                bank_account = json.load(f)
            return bank_account
  
    async def check_for_bank_account(self, ctx, send, member):

        user = member

        bank_account = await self.get_bank_data()

        if str(user.id) in bank_account:
            return False  
        else:
            await send("Use /create_bank_account to create a bank account")
            return

    async def hash_password(self, password):
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    async def verify_password(self, stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    async def new_bank_account(self, ctx, send, member, password):
        user = member
        bank_account = await self.get_bank_data()
        password = await self.hash_password(password)
        if str(user.id) in bank_account:
          
            await send("You already have a bank account, to reset your Password use /reset_bank_password")
            return False
        else:  
          
            bank_account[str(user.id)] = {}
            bank_account[str(user.id)]["money"] = 0
            bank_account[str(user.id)]["password"] = password

        file = open('bank.json', 'w', encoding='utf-8');
        file.write(json.dumps(bank_account, cls=MyEncoder, indent=4))
        file.close()
        #with open("bank.json", "w") as f:
        #    json.dump(bank_account,f)
        
        await send(f"Successfully created your bank account. (If you forget your Password, use `/reset_bank_password)`", ephemeral=True)
        return True 


    async def update_bank(self, member, send, amount, mode):

        user = member

        bank_account = await self.get_bank_data()
        users_coins = await self.get_coins()

        if mode == "bank":
            bank_money_amount = bank_account[str(user.id)]["money"]

            if amount > bank_money_amount:
                await send("You dont have enough money")

            bank_account[str(user.id)] += amount  
              
        elif mode == "wallet":
            wallet_money_amount = users_coins[str(user.id)]

            if amount > wallet_amount:
                await send("You dont have enough money")
                return

            #users_coins[str(user.id)] += amount

        
         
    

def setup(client):
    client.add_cog(banktransfer(client))