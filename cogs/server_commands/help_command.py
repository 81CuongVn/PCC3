import discord
from discord.ext import commands
from discord.ui import Button, View
import asyncio

class help_command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(name="help_test", invoke_without_command=True)
    async def help_group(self, ctx): 

        await ctx.message.delete()

        button_forward = Button(style=discord.ButtonStyle.primary, emoji="➡")
        button_back = Button(style=discord.ButtonStyle.primary, emoji="⬅")
        view = View()
        view.add_item(button_back)
        view.add_item(button_forward)

        embed = discord.Embed(title="Help", description="PC Creator", color=13565696)
        embed.add_field(name=f",scores (cpu, gpu, ram or all)", value="Shows charts with benchmark of CPUs, GPUs or RAM", inline=False)
        embed.add_field(name=f",optimize/opt", value="Sends a helpful text about optimize task", inline=False)
        embed.add_field(name=f",btcpc (bitcoinpc)", value="Shows a chart with good mining setups for every level", inline=False)
        embed.add_field(name=f",quantum", value="Sends a picture of a quantum PC in-game", inline=False)
        embed.add_field(name=f",cc (customcpu)", value="Will return a picture and a short explanation about custom CPUs", inline=False)
        embed.add_field(name=f",main", value="Shows a picture of the main screen in game with information about the buttons", inline=False)
        embed.add_field(name=f",record", value="Sends a picture and information about the best PC in PCC1", inline=False)

        embed_server = discord.Embed(title="Help", description="Discord server/bot commands", color=13565696)
        embed_server.add_field(name=f",lrs", value="Shows your levelroles progress", inline=False)
        embed_server.add_field(name=f",leaderboard", value="Shows the ,lrs leaderboard", inline=False)
        embed_server.add_field(name=f",whois", value="Gives information about the member such as join date", inline=False)
        embed_server.add_field(name=f",suggest", value="Can be used to suggest in the #suggestion channel", inline=False)
        embed_server.add_field(name=f",credits", value="Shows bot developer(s)/owner", inline=False)
        embed_server.add_field(name=f",staff", value="Sends an embed with all staff members", inline=False)
        embed_server.add_field(name=f",ping", value="Will return the ping of the bot", inline=False)
        embed_server.add_field(name=f",uptime", value="shows the uptime of the bot", inline=False)
        embed_server.add_field(name=f",note", value="Note stuff", inline=False)

        button_back.disabled = True
        message = await ctx.send(embed=embed, view=view, delete_after=60)  

        async def button_forward_callback(interaction):
            if interaction.user != ctx.author:
                return
            button_back.disabled = False
            button_forward.disabled = True
            await message.edit(embed=embed_server, view=view)

        async def button_back_callback(interaction):
            if interaction.user != ctx.author:
                return
            button_forward.disabled = False
            button_back.disabled = True
            await message.edit(embed=embed, view=view)    

        button_forward.callback = button_forward_callback
        button_back.callback = button_back_callback


        


    @help_group.command()
    async def ban(self, ctx):
        embed = discord.Embed(title=f"__Command: Ban__", description=f":small_blue_diamond: Name & usage: `/ban <member ID / mention>` \n\n:small_blue_diamond: Description: Only for moderation. Ban members \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed) 

    @help_group.command(aliases=["bitcoinpc", "miner"])
    async def btcpc(self, ctx):
        embed = discord.Embed(title=f"__Command: Bitcoinpc__", description=f":small_blue_diamond: Name & usage: `,bitcoinpc` \n\n:small_blue_diamond: Description: This command will send a chart with the best mining setups for every level \n\n:small_blue_diamond: Aliases: `,btcpc/,miner`", color=13565696)
        await ctx.send(embed=embed)

    @help_group.command()
    async def cost(self, ctx):
        embed = discord.Embed(title=f"__Command: Cost__", description=f":small_blue_diamond: Name & usage: `,cost` \n\n:small_blue_diamond: Description: This command will send a embed with information about the price of PCC2 \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)
        
    @help_group.command(aliases=["credits"])
    async def credit(self, ctx):
        embed = discord.Embed(title=f"__Command: Credits__", description=f":small_blue_diamond: Name & usage: `,credits` \n\n:small_blue_diamond: Description: Just information about the bot owner/developers \n\n:small_blue_diamond: Aliases: `,credit`", color=13565696)
        await ctx.send(embed=embed)    

    @help_group.command(aliases=["cc"])
    async def customcpu(self, ctx):
        embed = discord.Embed(title=f"__Command: Custom CPU__", description=f":small_blue_diamond: Name & usage: `,customcpu` \n\n:small_blue_diamond: Description: This command will return a picture and a small text about custom CPUs \n\n:small_blue_diamond: Aliases: `,cc`", color=13565696)
        await ctx.send(embed=embed)    

    @help_group.command(aliases=["help"])
    async def help_command(self, ctx):
        embed = discord.Embed(title=f"__Command: Help__", description=f":small_blue_diamond: Name & usage: `,help <command>` \n\n:small_blue_diamond: Description: This command will give you information about commands \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)    

    @help_group.command()
    async def kick(self, ctx):
        embed = discord.Embed(title=f"__Command: Kick__", description=f":small_blue_diamond: Name & usage: `/kick <member ID / ping the member` \n\n:small_blue_diamond: Description: Only for moderation \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)    

    @help_group.command(aliases=["lrs"])
    async def levelroles(self, ctx):
        embed = discord.Embed(title=f"__Command: Levelroles__", description=f":small_blue_diamond: Name & usage: `,levelroles <member ID or ping>` \n\n:small_blue_diamond: Description: This command will give you information about your current levelroles progress (mention a member to get his/her current progress) \n\n:small_blue_diamond: Aliases: `,lrs`", color=13565696)
        await ctx.send(embed=embed)

    @help_group.command()
    async def levels(self, ctx):
        embed = discord.Embed(title=f"__Command: Levels__", description=f":small_blue_diamond: Name & usage: `,levels` \n\n:small_blue_diamond: Description: This command will send a chart about levels in PCC1 \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)    

    @help_group.command()
    async def main(self, ctx):
        embed = discord.Embed(title=f"__Command: Main__", description=f":small_blue_diamond: Name & usage: `,main` \n\n:small_blue_diamond: Description: This command will show a picture with information about the main screen in PCC1 \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)

    @help_group.command(aliases=["opt"])
    async def optimize(self, ctx):
        embed = discord.Embed(title=f"__Command: Optimize__", description=f":small_blue_diamond: Name & usage: `,optimize` \n\n:small_blue_diamond: Description: This command will send a text about optimizing and a chart with some setups and the FPS they reach \n\n:small_blue_diamond: Aliases: `,opt`", color=13565696)
        await ctx.send(embed=embed)

    @help_group.command()
    async def ping(self, ctx):
        embed = discord.Embed(title=f"__Command: Ping__", description=f":small_blue_diamond: Name & usage: `,ping` \n\n:small_blue_diamond: Description: This command will show the ping of the bot \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)        

    @help_group.command(aliases=["ppra"])
    async def proplayeraddrole(self, ctx):
        embed = discord.Embed(title=f"__Command: PPRA__", description=f":small_blue_diamond: Name & usage: `,ppra <member Id / mention>` \n\n:small_blue_diamond: Description: This command will give PRO Player role to a member of the server \n\n:small_blue_diamond: Aliases: `,proplayeraddrole`", color=13565696)
        await ctx.send(embed=embed)    

    @help_group.command()
    async def quantum(self, ctx):
        embed = discord.Embed(title=f"__Command: Quantum__", description=f":small_blue_diamond: Name & usage: `,quantum` \n\n:small_blue_diamond: Description: This command will return a picture of a quantum PC \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)  

    @help_group.command()
    async def record(self, ctx):
        embed = discord.Embed(title=f"__Command: Record__", description=f":small_blue_diamond: Name & usage: `,record` \n\n:small_blue_diamond: Description: This command will send information about the current world record PC \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)      

    @help_group.command()
    async def scores(self, ctx):
        embed = discord.Embed(title=f"__Command: Scores__", description=f":small_blue_diamond: Name & usage: `,scores <CPU / GPU / RAM / All>` \n\n:small_blue_diamond: Description: This command will return charts with information about CPU, GPU or RAM. (For example the highest possible overclock) \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)   

    @help_group.command()
    async def softban(self, ctx):
        embed = discord.Embed(title=f"__Command: Softban__", description=f":small_blue_diamond: Name & usage: `/softban` \n\n:small_blue_diamond: Description: For moderation only. Use /softban then use the member ID or mention the member to softban him (ban & instant unban) \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)  

    @help_group.command()
    async def staff(self, ctx):
        embed = discord.Embed(title=f"__Command: Staff__", description=f":small_blue_diamond: Name & usage: `,staff` \n\n:small_blue_diamond: Description: This command will return an embed with all staff members in it \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)     

    @help_group.command(aliases=["suggest"])
    async def suggestions(self, ctx):
        embed = discord.Embed(title=f"__Command: Suggest__", description=f":small_blue_diamond: Name & usage: `,suggest <content>` \n\n:small_blue_diamond: Description: Create a suggestion. Only works in #suggestions. \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)     

    @help_group.command()
    async def timeout(self, ctx):
        embed = discord.Embed(title=f"__Command: Timeout__", description=f":small_blue_diamond: Name & usage: `/timeout <member Id / mention>` \n\n:small_blue_diamond: Description: For moderation only. Use /timeout then use the member ID or mention the member to send him in a timeout \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)  

    @help_group.command()
    async def unban(self, ctx):
        embed = discord.Embed(title=f"__Command: Unban__", description=f":small_blue_diamond: Name & usage: `,unban <member name>` \n\n:small_blue_diamond: Description: Use ,unban to unban people. You have to do ,unban <member Name> don't use the ID. You have to do for example ,unban ¥£$#7660 \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)    

    @help_group.command()
    async def unmute(self, ctx):
        embed = discord.Embed(title=f"__Command: Unmute__", description=f":small_blue_diamond: Name & usage: `/unmute <member ID / mention>` \n\n:small_blue_diamond: Description: Use ,unmute to unmute a member \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)   

    @help_group.command()
    async def uptime(self, ctx):
        embed = discord.Embed(title=f"__Command: Uptime__", description=f":small_blue_diamond: Name & usage: `,uptime` \n\n:small_blue_diamond: Description: This command will return the uptime of the bot (How long the bot was online) \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)       

    @help_group.command()
    async def whois(self, ctx):
        embed = discord.Embed(title=f"__Command: Whois__", description=f":small_blue_diamond: Name & usage: `,whois <member ID / mention>` \n\n:small_blue_diamond: Description: Use ,whois to get information about a member like their join date \n\n:small_blue_diamond: Aliases: No aliases", color=13565696)
        await ctx.send(embed=embed)     


def setup(client):
    client.add_cog(help_command(client))