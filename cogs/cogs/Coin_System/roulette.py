import discord
from discord.ext import commands
from discord import Option
from bank_functions import check_for_bank_account, get_bank_data, get_coins, update_bank
import json
import random

class roulette(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="roulette", description="Play the classic roulette game")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def roulette_slash(self, ctx, amount : Option(int, required=True), guess: Option(str, 'Choose', choices=['Red', 'Black', 'Green', 'Number'], required=True)):#, password : Option(int, required=True)):
        send = ctx.respond
        member = ctx.author
        user = member
        users_coins = await get_coins()
        wallet_amt = users_coins[str(user.id)]
        mode = "wallet"
        win = random.randrange(0,37)

        if amount <= 0:
          await ctx.respond(f"You can't use {amount}<:bot_icon:951868023503986699>")
          return

        if amount > wallet_amt:
            await ctx.respond(f"You dont have enough money")
            return

        print(win)
        if guess == 'Red':
            if win >= 1 and win <= 18:
                await ctx.respond(f"You won {amount}<:bot_icon:951868023503986699> <:Stonksup:712232686441463828>")
                await update_bank(member, send, amount, mode)
            else:
                await ctx.respond(f"You lost {amount}<:bot_icon:951868023503986699>")
                await update_bank(member, send, -1*amount, mode)
        print(win)      

        if guess == 'Black':
            print(win)
            if 19 >= win and win <= 36:
                await ctx.respond(f"You won {amount}<:bot_icon:951868023503986699> <:Stonksup:712232686441463828>")
                await update_bank(member, send, amount, mode)
            else:
                await ctx.respond(f"You lost {amount}<:bot_icon:951868023503986699>")
                await update_bank(member, send, -1*amount, mode)

        if guess == 'Green':
            if win == 0:
              await ctx.respond(f"You won {10*amount}<:bot_icon:951868023503986699> <:Stonksup:712232686441463828>")
              await update_bank(member, send, 10*amount, mode)
            else:
                await ctx.respond(f"You lost {amount}<:bot_icon:951868023503986699>")
                await update_bank(member, send, -1*amount, mode)  

        if guess == 'Number':
            await ctx.respond("Choose a number between 0 and 36")
            number = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
            number = number.content
            if number == win:
                await ctx.send(f"You won {10*amount}<:bot_icon:951868023503986699> <:Stonksup:712232686441463828>")
                await update_bank(member, send, 10*amount, mode)
            else:
                await ctx.send(f"You lost {amount}<:bot_icon:951868023503986699> \nThe right number was {win}")
                await update_bank(member, send, -1*amount, mode)
            

        #bank_account[str(user.id)]["money"] += amount
        #users_coins[str(user.id)] += -1*amount

        #with open("bank.json", "w") as f:
        #    json.dump(bank_account,f)

        #with open("usercoins.json", "w") as f:
        #    json.dump(users_coins,f)  


def setup(client):
    client.add_cog(roulette(client))  