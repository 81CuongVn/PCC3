import discord
from discord.ext import commands
from discord import Option
from bank_functions import get_useritems, get_coins, get_bank_data
import json

class inventory(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="inventory", description="What do you have?")
    async def bal_slash_command(self, ctx, member: Option(discord.Member, required = False)):
        if member == None:
            member = ctx.author
        send = ctx.respond
        user = member
        items = await get_useritems()
        coins = await get_coins()
        bank_account = await get_bank_data()
        embed = discord.Embed(title=f"{member}'s inventory", color=13565696)
        if str(user.id) in items:
            items_str = items[str(user.id)]
            items_str = '\n'.join(items_str)
            if str(user.id) in coins:
                coins = coins[str(user.id)]
                embed.add_field(name="Coins", value=f"{coins}<:bot_icon:951868023503986699>")
            else:
                embed.add_field(name="Coins", value="0<:bot_icon:951868023503986699>")
            if str(user.id) in bank_account:
                bank_coins=bank_account[str(user.id)]["money"]
                embed.add_field(name="Bank", value=f"{bank_coins}<:bot_icon:951868023503986699>")
            else:
                embed.add_field(name="Bank", value="0<:bot_icon:951868023503986699>")
            embed.add_field(name="Items", value=f"{items_str}")
        else:
            if str(user.id) in coins:
                coins = coins[str(user.id)]
                embed.add_field(name="Coins", value=f"{coins}<:bot_icon:951868023503986699>")
            else:
                embed.add_field(name="Coins", value="0<:bot_icon:951868023503986699>")  
            if str(user.id) in bank_account:
                bank_coins=bank_account[str(user.id)]["money"]
                embed.add_field(name="Bank", value=f"{bank_coins}<:bot_icon:951868023503986699>")
            else:
                embed.add_field(name="Bank", value="0<:bot_icon:951868023503986699>")  
            embed.add_field(name="Items", value="None")
        try:
            embed.set_thumbnail(url=member.avatar.url)
        except:
            pass
        #await ctx.respond('This command is currently out of order. Use /balance or ,bal to see your Money.')
        await send(embed=embed)


def setup(client):
    client.add_cog(inventory(client)) 