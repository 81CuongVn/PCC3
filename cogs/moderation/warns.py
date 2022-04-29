import discord
from discord.ext import commands
from discord.commands import permissions
from discord import Option
import json

rolelist = [589435378147262464, 648546626637398046, 632674518317531137, 571032502181822506, 697002610892341298]

class warns(commands.Cog):

    def __init__(self, client):
        self.client = client

 
    @commands.slash_command(name="warn", description="For Moderation")
    async def warn(self, ctx, member: Option(discord.Member, required = True), reason: Option(str, required=True)):    
        user = ctx.author
        if any(role.id in rolelist for role in user.roles):
            await self.new_warn_member(member)
            await self.update_warns(member, reason)
            await ctx.respond(f"Warned {member.mention} for {reason}")
        else:
            return



    @commands.slash_command(name="modlogs", description="Check the warns/mutes etc. of a member")      
    async def modlogs(self, ctx, member: Option(discord.Member, required = False)):
        if member.id not in []:

            if member == None:
                member = ctx.author

            await self.new_warn_member(member)
            warns = await self.get_warns()

            warn_count = warns[str(member.id)]["warn_count"] 
            warn_count_1 = warns[str(member.id)]["warn_count"] + 1 

            mute_count = warns[str(member.id)]["mute_count"]
            mute_count_1 = warns[str(member.id)]["mute_count"] + 1

            ban_count = warns[str(member.id)]["ban_count"]
            ban_count_1 = warns[str(member.id)]["ban_count"] + 1

            kick_count = warns[str(member.id)]["kick_count"]  
            kick_count_1 = warns[str(member.id)]["kick_count"] + 1

            embed = discord.Embed(title=f"{member.name}'s modlogs", description=f"warn count: {warn_count} \nmute count: {mute_count} \nkick count: {kick_count} \nban count: {ban_count}", color=13565696)
            try:    
                embed.set_thumbnail(url=member.avatar.url)
            except:
                pass    
        
            try:
                for x in range(1,warn_count_1):
                    warn_reason = warns[str(member.id)][f"warn {x}"]
                    embed.add_field(name=f"warn {x}:", value=warn_reason, inline=False)    
            except:
                pass

            try:    
                for x in range(1,mute_count_1):
                    mute_reason = warns[str(member.id)][f"mute {x}"]
                    embed.add_field(name=f"mute {x}:", value=mute_reason, inline=False)
            except:
                pass

            try:
                for x in range(1,kick_count_1):
                    kick_reason = warns[str(member.id)][f"kick {x}"]
                    embed.add_field(name=f"kick {x}:", value=kick_reason, inline=False)
            except:
                pass

            try:
                for x in range(1,ban_count_1):
                    ban_reason = warns[str(member.id)][f"ban {x}"]
                    embed.add_field(name=f"ban {x}:", value=ban_reason, inline=False)      
            except:
                pass 

            await ctx.respond(embed=embed)
        else:
            if member == None:
                member = ctx.author

            await self.new_warn_member(member)
            warns = await self.get_warns()

            warn_count = warns[str(member.id)]["warn_count"] 
            warn_count_1 = warns[str(member.id)]["warn_count"] + 1 

            mute_count = warns[str(member.id)]["mute_count"]
            mute_count_1 = warns[str(member.id)]["mute_count"] + 1

            ban_count = warns[str(member.id)]["ban_count"]
            ban_count_1 = warns[str(member.id)]["ban_count"] + 1

            kick_count = warns[str(member.id)]["kick_count"]  
            kick_count_1 = warns[str(member.id)]["kick_count"] + 1

            embed = discord.Embed(title=f"{member.name}'s modlogs", description=f"warn count: {warn_count} \nmute count: {mute_count} \nkick count: {kick_count} \nban count: {ban_count}", color=13565696)
            try:    
                embed.set_thumbnail(url=member.avatar.url)
            except:
                pass    

            warn_reason = ""
            try:
                for x in range(1,warn_count_1):
                    warn_reason += ", " +  warns[str(member.id)][f"warn {x}"]
                embed.add_field(name=f"warn {x}:", value=warn_reason, inline=False)
            except:
                pass

            mute_reason = ""
            try:    
                for x in range(1,mute_count_1):
                    mute_reason += ", " + warns[str(member.id)][f"mute {x}"]
                embed.add_field(name=f"mute {x}:", value=mute_reason, inline=False)
            except:
                pass

            kick_reason = ""
            try:
                for x in range(1,kick_count_1):
                    kick_reason += ", " +  warns[str(member.id)][f"kick {x}"]
                embed.add_field(name=f"kick {x}:", value=kick_reason, inline=False)
            except:
                pass

            ban_reason = ""
            try:
                for x in range(1,ban_count_1):
                    ban_reason += ", " +  warns[str(member.id)][f"ban {x}"]
                embed.add_field(name=f"ban {x}:", value=ban_reason, inline=False)   
            except:
                pass 

            await ctx.respond(embed=embed)

                 
            

           

    async def get_warns(self):
        with open("json_files/warns.json", "r") as f:
                warns = json.load(f)
        return warns

    async def new_warn_member(self, member):

            warns = await self.get_warns()

            if str(member.id) in warns:
                return False
            else:
                warns[str(member.id)] = {}
                warns[str(member.id)]["warn_count"] = 0
                warns[str(member.id)]["mute_count"] = 0
                warns[str(member.id)]["ban_count"] = 0
                warns[str(member.id)]["kick_count"] = 0

            with open("json_files/warns.json", "w") as f:
                json.dump(warns,f)
            return True     

    async def update_warns(self, member, reason):

        warns = await self.get_warns()

        warn_count_old = warns[str(member.id)]["warn_count"]
        warn_count_new = warn_count_old + 1
        warns[str(member.id)]["warn_count"] = warn_count_new
        warns[str(member.id)][f"warn {warn_count_new}"] = reason    

        with open("json_files/warns.json", "w") as f:
            json.dump(warns,f)      

def setup(client):
    client.add_cog(warns(client)) 