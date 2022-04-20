import discord
from discord.ext import commands
from discord import Option
import json
from bank_functions import check_for_bank_account, get_bank_data, get_trading, get_trading_list, new_trading_member

class trading_check(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="ctrade")
    async def ctrade(self, ctx):
        trading_member = await get_trading()
        trading_list = await get_trading_list()
        open_trades = trading_member[str(ctx.author.id)]
        await ctx.send(open_trades)
        if len(open_trades) == 0:
            await ctx.send("You have no trade offers")
            return
        else:
            for i in range(len(open_trades)):
                trade_things = trading_list["trades"][str(open_trades[i])]["give_type"]
                print(trade_things)
                #trade_things_list = []
                #trade_things_list.append(trade_things)
                #await ctx.send(trade_things)"""


def setup(client):
    client.add_cog(trading_check(client))