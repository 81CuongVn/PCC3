import discord
from discord.ext import commands
from discord import Option
from bank_functions import get_coins, new_member
import random
import json

class luckywheel(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="luckywheel", description="Win something...")
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def luckywheel_slash(self, ctx, amount:Option(int, required=True)):
        member = ctx.author
        user = member
        await new_member(member)
        users_coins = await get_coins()
        coins_amt_str = users_coins[str(user.id)]
        coins_amt = int(coins_amt_str)

        if amount > coins_amt:
            await ctx.respond(f"You don't have enough money (You have {coins_amt}<:bot_icon:951868023503986699>)")
            return

        if amount <= 0:
            await ctx.respond(f"You can't use {amount}<:bot_icon:951868023503986699>")
            return    

        win = random.randrange(0,3)   
        money_before = users_coins[str(user.id)]

        if win == 0:
            money_after = money_before + 2*amount
            win_state =  "You won <:Stonksup:712232686441463828> <:Stonksup:712232686441463828>"
            won_word = "won"
            prize = 2*amount
            users_coins[str(user.id)] += prize

        if win == 1 or win == 2:
            money_after = money_before - amount
            win_state = "You lost <:Stonksdown:712232673342390303> <:Stonksdown:712232673342390303>" 
            won_word = "lost"
            prize = amount 
            prize_1 = -1*amount
            users_coins[str(user.id)] += prize_1
            
        with open("json_files/usercoins.json", "w") as f:
            json.dump(users_coins,f)
        embed= discord.Embed(title="Lucky wheel", color=member.color)
     
        embed.add_field(name=win_state, value=f"<@{member.id}> {won_word} {prize} \n\nYou had **{money_before}**<:bot_icon:951868023503986699> and now you have **{money_after}**<:bot_icon:951868023503986699>")

        try:
                embed.set_thumbnail(url=member.avatar.url)
        except:
            pass
        await ctx.respond(embed=embed)


def setup(client):
    client.add_cog(luckywheel(client)) 