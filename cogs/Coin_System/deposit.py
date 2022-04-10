import discord
from discord.ext import commands
from discord import Option
from bank_functions import check_for_bank_account, get_bank_data, get_coins, verify_password
import json

class deposit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="deposit", description="Transfer your money from your wallet into your bank account")
    async def deposit_slash(self, ctx, password: Option(str, required=True), amount : Option(int, required=True)):#, password : Option(int, required=True)):
        send = ctx.respond
        member = ctx.author
        user = member
        await check_for_bank_account(ctx, send, member)
        bank_account = await get_bank_data()
        users_coins = await get_coins()
        if str(user.id) in bank_account: #750iq move hilft immer
            bank_amt = bank_account[str(user.id)]["money"]
        else:
            return
        wallet_amt = users_coins[str(user.id)]

        if amount <= 0:
          await ctx.respond(f"You can't deposit {amount} <:bot_icon:951868023503986699>", ephemeral=True)
          return

        if amount > wallet_amt:
            await ctx.respond(f"You dont have enough money (You have {wallet_amt}<:bot_icon:951868023503986699>)", ephemeral=True)
            return

        stopwd = bank_account[str(user.id)]["password"]
        verified_pwd = await verify_password(stopwd, password)
        if verified_pwd == 'yes':
            bank_account[str(user.id)]["money"] += amount
            users_coins[str(user.id)] += -1*amount

            with open("json_files/bank.json", "w") as f:
                json.dump(bank_account,f)
    
            with open("json_files/usercoins.json", "w") as f:
                json.dump(users_coins,f)

            await ctx.respond(f"You deposited {amount}<:bot_icon:951868023503986699>", ephemeral=True)  

        else:
            await ctx.respond(f"Wrong Password", ephemeral=True)
            

def setup(client):
    client.add_cog(deposit(client))  