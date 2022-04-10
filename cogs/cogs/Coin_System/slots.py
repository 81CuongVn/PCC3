import discord
from discord.ext import commands
from discord import Option
import json
import random
from bank_functions import new_member, get_coins
from datetime import datetime

class slots(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="slots", description="Try your luck at the slots machine")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def slots(self, ctx, amount : Option(int, required=True)):

        member = ctx.author
      
        await new_member(member)
    
        users_coins = await get_coins()
    
        coins_amt = users_coins[str(member.id)]

      
        if amount > coins_amt:
            await ctx.respond(f"You don't have enough money (You have {coins_amt}<:bot_icon:951868023503986699>)")
            return
        elif amount <= 0:
            await ctx.respond(f"You can't use {amount}<:bot_icon:951868023503986699>")
            return
  
        slot1 = random.choice(["👍", "❌", "💯", "🎱", "🍎", "🍓", "🥇" ])
        slot2 = random.choice(["👍", "❌", "💯", "🎱", "🍎", "🍓", "🥇" ])
        slot3 = random.choice(["👍", "❌", "💯", "🎱", "🍎", "🍓", "🥇" ])

        old_amount = users_coins[str(member.id)]
    
        if slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
            if slot1 == slot2 and slot2 == slot3: # chance is 1% (so technically you would have to win 35x to have no losses)
                t_amount = 15*amount
                new_amount = users_coins[str(member.id)] + 15*amount
                users_coins[str(member.id)] += 15*amount
            else: # chance of getting is ~ 14% so  3.5 times the money equals to a 2% money loss per game (if you win 14% of the time)
                t_amount = 2*amount
                new_amount = users_coins[str(member.id)] + 2*amount
                users_coins[str(member.id)] += 2*amount
            embed=discord.Embed(title="Slot Machine", colour=ctx.author.colour, timestamp=datetime.now())
            embed.add_field(name=f"{slot1}  {slot2}  {slot3}", value=f"You won **{t_amount}**<:bot_icon:951868023503986699> 🥳 \nYou had **{old_amount}**<:bot_icon:951868023503986699> \nNow you have **{new_amount}**<:bot_icon:951868023503986699>", inline=False)
            await ctx.respond(embed = embed)
            with open("usercoins.json", "w") as f:
                json.dump(users_coins,f)
            return
        else:
            new_amount = users_coins[str(member.id)] + -1*amount
            users_coins[str(member.id)] += -1*amount  
            embed=discord.Embed(title="Slot Machine", colour=ctx.author.colour, timestamp=datetime.now())
            embed.add_field(name=f"{slot1}  {slot2}  {slot3}", value=f"You lost **{amount}**<:bot_icon:951868023503986699> 😕\nYou had **{old_amount}**<:bot_icon:951868023503986699> \nNow you have **{new_amount}**", inline=False)
            await ctx.respond(embed = embed)
            with open("usercoins.json", "w") as f:
                json.dump(users_coins,f)
            return
          
def setup(client):
    client.add_cog(slots(client)) 