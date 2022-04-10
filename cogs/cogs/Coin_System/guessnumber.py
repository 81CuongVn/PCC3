import discord
from discord.ext import commands
from discord import Option
from bank_functions import new_member, get_coins, update_bank
import json
import random

class guessnumber(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="guessnumber", description="Guess the number")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def guessnumber_slash(self, ctx, amount: Option(int, required=True), number: Option(int, "Choose a number between 1 and 10", required=True)):
        member = ctx.author      
        await new_member(member)
        user = member
        users_coins = await get_coins()
        coins_amt_str = users_coins[str(user.id)]
        coins_amt = int(coins_amt_str)
        send = ctx.respond

        if amount <= 0:
            await ctx.respond(f"You can't use {amount}<:bot_icon:951868023503986699>")
            return

        if amount > coins_amt:
            await ctx.respond(f"You dont have that much money (You have {coins_amt}<:bot_icon:951868023503986699>)")  
            return

        if number > 10:
            await ctx.respond("You can only use numbers between 1 and 10")
            return

        guessnumber = random.randrange(0,11)   

        if number == guessnumber:
            await ctx.respond(f"That's right <:pog:813886729235988541> \nYou won {2*amount}<:bot_icon:951868023503986699>")
            await update_bank(member, send, 2*amount, mode)
        else:
            await ctx.respond(f"I'm sorry but that's wrong. The right answer is {guessnumber} \nYou lost {amount}<:bot_icon:951868023503986699>") 
            await update_bank(member, send, -1*amount, mode)


def setup(client):
    client.add_cog(guessnumber(client)) 