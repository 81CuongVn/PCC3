import discord
from discord.ext import commands
from discord.ui import Button, View
from discord import Option


class DroppDownMenu(discord.ui.View):
    @discord.ui.select(placeholder="Choose one option", min_values=1, max_values=1, options=[
       discord.SelectOption(label="CPU", description="The CPUs scores list"),
        discord.SelectOption(label="GPU", description="The GPUs scores list"),
        discord.SelectOption(label="RAM", description="The RAMs scores list"),
        discord.SelectOption(label="All", description="All scores lists")
    ])
    async def callback(self, select, interaction : discord.Interaction):
        if select.values[0] == "CPU":
            await interaction.response.send_message("https://media.discordapp.net/attachments/838857610358292532/931919636461654046/CPU-Scores_Super_Dark_Mode_3.jpg")
        if select.values[0] == "GPU":
            await interaction.response.send_message("https://media.discordapp.net/attachments/838857610358292532/931919674134904982/GPU_Scores_Super_Dark_Mode_5.jpg")
        if select.values[0] == "RAM":
            await interaction.response.send_message("https://media.discordapp.net/attachments/838857610358292532/931919651070423100/RAM_scores_Super_Dark_Mode_4.jpg")
        if select.values[0] == "All":
            await interaction.response.send_message("https://media.discordapp.net/attachments/838857610358292532/931919636461654046/CPU-Scores_Super_Dark_Mode_3.jpg")        
            await interaction.followup.send("https://media.discordapp.net/attachments/838857610358292532/931919674134904982/GPU_Scores_Super_Dark_Mode_5.jpg")
            await interaction.followup.send("https://media.discordapp.net/attachments/838857610358292532/931919651070423100/RAM_scores_Super_Dark_Mode_4.jpg")

class scores(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def scores(self, ctx, reason = None):
        try:
            if reason.lower() == "cpu":
                await ctx.send("https://media.discordapp.net/attachments/838857610358292532/931919636461654046/CPU-Scores_Super_Dark_Mode_3.jpg") 
            if reason.lower() == "gpu":
                await ctx.send("https://media.discordapp.net/attachments/838857610358292532/931919674134904982/GPU_Scores_Super_Dark_Mode_5.jpg")  
            if reason.lower() == "ram":
                await ctx.send("https://media.discordapp.net/attachments/838857610358292532/931919651070423100/RAM_scores_Super_Dark_Mode_4.jpg")

        except:
            await self.scores_buttons(ctx)

    async def scores_buttons(self, ctx):    
        button_cpu = Button(label="CPU", style=discord.ButtonStyle.primary)
        button_gpu = Button(label="GPU", style=discord.ButtonStyle.primary)
        button_ram = Button(label="RAM", style=discord.ButtonStyle.primary)
        button_all = Button(label="All", style=discord.ButtonStyle.primary)

        view = View()
        view.add_item(button_cpu)
        view.add_item(button_gpu)
        view.add_item(button_ram)
        view.add_item(button_all)


        message = await ctx.send('Which component chart would you like to view? Respond with "CPU", "GPU", "RAM" or "all" (20s)', view=view)

        async def button_cpu_callback(interaction:discord.Interaction):
            await message.edit(content="https://media.discordapp.net/attachments/802512035224223774/948613482922782750/CPU-Scores_Super_Dark_Mode_4.jpg", view=None)

        async def button_gpu_callback(interaction:discord.Interaction):
            await message.edit(content="https://media.discordapp.net/attachments/802512035224223774/948613531320860773/GPU_Scores_Super_Dark_Mode_6.jpg", view=None)
        async def button_ram_callback(interaction:discord.Interaction):
            await message.edit(content="https://media.discordapp.net/attachments/802512035224223774/948613542360256562/RAM_scores_Super_Dark_Mode_5.jpg", view=None)

        async def button_all_callback(interaction:discord.Interaction):
            await message.edit(content="https://media.discordapp.net/attachments/802512035224223774/948613482922782750/CPU-Scores_Super_Dark_Mode_4.jpg", view=None)            
            await ctx.send("https://media.discordapp.net/attachments/802512035224223774/948613531320860773/GPU_Scores_Super_Dark_Mode_6.jpg")
            await ctx.send("https://media.discordapp.net/attachments/802512035224223774/948613542360256562/RAM_scores_Super_Dark_Mode_5.jpg")

        button_cpu.callback = button_cpu_callback
        button_gpu.callback = button_gpu_callback
        button_ram.callback = button_ram_callback
        button_all.callback = button_all_callback

    @commands.slash_command(name='scores_pcc1', description='Shows charts with benchmark of CPUs, GPUs or RAM')
    async def pcc1_scores_slash(self, ctx, part: Option(str, 'Choose the parts you need', choices=['CPU', 'GPU', 'RAM', 'All'], required=True)):
        if part in ('CPU', 'All'):
            await ctx.respond("https://media.discordapp.net/attachments/802512035224223774/948613482922782750/CPU-Scores_Super_Dark_Mode_4.jpg")
        if part in ('GPU', 'All'):
            await ctx.respond("https://media.discordapp.net/attachments/802512035224223774/948613531320860773/GPU_Scores_Super_Dark_Mode_6.jpg")
        if part in ('RAM', 'All'):
            await ctx.respond("https://media.discordapp.net/attachments/802512035224223774/948613542360256562/RAM_scores_Super_Dark_Mode_5.jpg")

        

def setup(client):
    client.add_cog(scores(client))            