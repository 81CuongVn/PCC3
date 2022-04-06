import discord
from discord.ext import commands
from discord import Option
from bank_functions import bal, change_coins, verify_password, get_bank_data, hash_password, bank_bal
import json

class transfer(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="transfer", description="Transfers money to another user")
    async def transfer_slash(self, ctx, password: Option(str, required=True),  member: Option(discord.Member, required=True), amount: Option(int, required=True)):
        user = ctx.author
        userbal = await bank_bal(ctx, user)
       # user = member
        memberbal = await bank_bal(ctx, member)
       # user = ctx.author
        bankdata = await get_bank_data()
        if str(user.id) in bankdata:

            if amount <= 0:
                await ctx.respond("You can only send a positive amount of money", ephemeral=True)
                return

            stored_user = bankdata[str(user.id)]
            stored_pass = stored_user['password']
            verpass = await verify_password(stored_pass, password)
            if verpass == 'yes':
                if userbal >= amount:
                    
                    subtract = True
                    await change_coins(ctx, user, amount, subtract)
                    subtract = False
                    await change_coins(ctx, member, amount, subtract)
                    await ctx.respond(f"You sent **{amount}**<:bot_icon:951868023503986699> successfully to <@{member.id}>.", ephemeral=True)
                    await ctx.send(f"<@{user.id}> sent <@{member.id}> **{amount}**<:bot_icon:951868023503986699>")
                    #try:
                        #await self.client.send_message(member, f"You got **{amount}**<:bot_icon:951868023503986699> from <@{user.id}>.")
                    #except:
                        #print(f"Could not send message 'You got **{amount}**<:bot_icon:951868023503986699> from <@{user.id}>.' to {member.id}")
                else:
                    await ctx.respond("You don't have enough coins to do that. Use /balance to see your coins.", ephemeral=True)
            elif verpass == 'no':
                await ctx.respond("Your provided password is wrong. To reset it use `/reset_bank_password`", ephemeral=True)
            else:
                botdev_role = discord.utils.get(ctx.channel.guild.roles, id=951207540472029195)
                await ctx.respond(f"The bot had a catastrophic failure whilst processing your password. Please try again in a few minutes. If the error persists, please contact a Bot Developer", ephemeral=True)

        else:
            await ctx.respond('You do not have a bank account yet. Create one using `/create_bank_account`')


def setup(client):
    client.add_cog(transfer(client)) 