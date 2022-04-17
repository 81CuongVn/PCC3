from tabnanny import check
import discord
from discord.ext import commands
from datetime import datetime
from datetime import timedelta
from datetime import date
from discord.ext.commands import MemberNotFound
import json
from discord import Option
class whois(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="whois")
    async def whois_normal_command(self, ctx, member:discord.Member = None):
        send = ctx.send
        await self.whois(ctx , send, member)


    @commands.slash_command(name="whois", description="Gives information about the mumber such as join date")
    async def whois_slash_command(self, ctx, member: Option(discord.Member, required = False)):
        send = ctx.respond
        await self.whois(ctx , send, member)      

    async def whois(self, ctx, send, member:discord.Member = None):
        #await test_187()
        #await new_restriction(ctx)
        #await check_server_restriction(ctx)
        
        #if await check_server_restriction(ctx):  # the == True can be omitted
        #    print("Nicht perint")
        #    return

        if member == None:
            member = ctx.author

        
        role_ids = [571032502181822506, 632674518317531137, 697728131003580537]    

        member_created = member.created_at.strftime("%m-%d-%Y")   
        date_now = date.today()
        create_date = member.created_at.date()
        delta_create = date_now - create_date
        delta_create_int = int(delta_create.days) 
        create_delta_shown = "days"

        member_joined = member.joined_at.strftime("%m-%d-%Y")   
        join_date = member.joined_at.date()
        delta_join = date_now - join_date
        delta_join_int = int(delta_join.days) 
        joined_delta_shown = "days"

        if delta_create_int >= 7:
            delta_weeks = float(delta_create.days/7)
            delta_create_int = int(delta_create.days/7)
            create_delta_shown = "weeks"
            if delta_weeks >= float(4.3):
                delta_month = int(delta_weeks/4.3)
                delta_create_int = int(delta_month)
                create_delta_shown = "months"
                if delta_month >= 12:
                    delta_years = int(delta_month/12)
                    delta_create_int = int(delta_years)
                    create_delta_shown = "years"

        if delta_join_int >= 7:
            delta_weeks2 = float(delta_join.days/7)
            delta_join_int = int(delta_join.days/7)
            joined_delta_shown = "weeks"
            if delta_weeks2 >= float(4.3):
                delta_month2 = int(delta_weeks2/4.3)
                delta_join_int = int(delta_month2)
                joined_delta_shown = "months"
                if delta_month2 >= 12:
                    delta_years2 = int(delta_month2/12)
                    delta_join_int = int(delta_years2)
                    joined_delta_shown = "years"            
        
        roles = [role.id for role in member.roles]
        rr = (['<@&{}> '.format(role) for role in roles][1:])
        rr2 = "\n".join([str(elem) for elem in rr])  
    
        if not rr:
            rr2 = "The member has no roles"


        embed = discord.Embed(title=f"{member.name}'s user info", color=member.color)
        embed.add_field(name=":small_blue_diamond: Account creation date", value=f"{member_created} (MM-DD-YYYY), {delta_create_int} {create_delta_shown} ago")
        embed.add_field(name=":small_blue_diamond: Join date", value=f"{member_joined} (MM-DD-YYY), {delta_join_int} {joined_delta_shown} ago", inline=False)
        embed.add_field(name=":small_blue_diamond: ID, Nickname, and Mention", value=f"ID: {member.id} \nNickname: {member.display_name} \nMention: {member.mention}", inline = False)
        embed.add_field(name=":small_blue_diamond: Roles", value=f"{rr2}", inline=False)
        try:
            embed.set_image(url=member.avatar.url)
        except:
            pass    
        await send(embed=embed)

        


def setup(client):
    client.add_cog(whois(client))
