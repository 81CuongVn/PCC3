import discord
from discord.ext import commands
from discord import Option
from bank_functions import get_bank_data, hash_password
import json

class reset_bank_password(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.slash_command(name="reset_bank_password", description="Resets your bank Password")
    async def reset_bank_pwd_slash_command(self, ctx, new_password:Option(str, required = True)):
        user = ctx.author
        bank_account = await get_bank_data()
        password = await hash_password(new_password)
        bank_account[str(user.id)]["password"] = password.decode("utf-8")

        file = open('bank.json', 'w', encoding='utf-8');
        file.write(json.dumps(bank_account, indent=4))
        file.close()

        await ctx.respond("Successfully reseted your bank password", ephemeral=True)


def setup(client):
    client.add_cog(reset_bank_password(client))