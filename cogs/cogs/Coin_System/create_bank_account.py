import discord
from discord.ext import commands
from discord import Option
from bank_functions import new_bank_account
import json

class create_bank_account(commands.Cog):

    def __init__(self, client):
        self.client = client

   
    @commands.slash_command(name="create_bank_account", description="Create a bank account to deposit and withdraw your coins")
    async def create_bank_account_slash(self, ctx, password: Option(str, required=True)):
        member = ctx.author
        send = ctx.respond
        printer = await new_bank_account(self, ctx, send, member, password)
        await ctx.respond(printer, ephemeral=True)

def setup(client):
    client.add_cog(create_bank_account(client))