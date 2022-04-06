import discord
from discord.ext import commands
from discord.ui import Button, View
import json
from discord import Option
from discord.commands import permissions

class nf_game(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def answer_yes(self):
        answer_yes = ["yes", "y", "ye", "yup"]
        return answer_yes

    async def answer_no(self):
        answer_no = ["no", "n", "nah", "nope"]
        return answer_no

    async def quest0(self, ctx):
        await ctx.respond("You are a nuclear reactor worker. Suddenly there is a power outage. Can you keep calm?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        ansn = await self.answer_no()
        if ans.content.lower() in ansy:
            await self.quest1(ctx)
        elif ans.content.lower() in ansn:
            await self.quest1no(ctx)
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def quest1no(self, ctx):
        await ctx.send("You're so scared you're going to faint. When you wake up, you're still in the nuclear reactor. You decide to pull yourself together and look for the cause.")
        await ctx.send("You walk around in the dark for a long time and find a lighter. Do you take it with you?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        ansn = await self.answer_no()
        if ans.content.lower() in ansy:
            await self.quest1noyes(ctx)
        elif ans.content.lower() in ansn:
            await self.quest1(ctx)
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def quest1noyes(self, ctx):
        await ctx.send("You wander around with the light of the flame of the lighter. Suddenly you smell gas. Do you turn off the lighter and keep wandering in the dark?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        ansn = await self.answer_no()
        if ans.content.lower() in ansy:
            await ctx.send("When you don't smell the gas anymore, you try to turn on the lighter, but it seems to be out of lighter fluid.")
            await self.quest1(ctx)
        elif ans.content.lower() in ansn:
            await self.death_by_gas_fire(ctx)
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")



    async def quest1(self, ctx):
        await ctx.send("After a bit of wandering around you discover discover a flashlight. Do you take it?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        if ans.content.lower() in ansy:
            await self.quest2(ctx)
        elif ans.content.lower() in ansn:
            await self.quest2no(ctx)
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def quest2no(self, ctx):
        await ctx.send("After a bit of wandering around you discover discover a flashlight. Do you take it?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        if ans.content.lower() in ansy:
            await self.quest2noyes(ctx)
        elif ans.content.lower() in ansn:
            await ctx.send("not yet implemented")
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def quest2(self, ctx):
        await ctx.send("You continue the search for the cause with the light of the flashlight. You see the control room. Do you enter it?")

        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        if ans.content.lower() in ansy:
            await self.quest3(ctx)
        elif ans.content.lower() in ansn:
            await ctx.send("not yet implemented")
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def quest3(self, ctx):
        await ctx.send("You see an LED that says EMERGENCY GENERATOR with a button underneath. Do you press the button?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        if ans.content.lower() in ansy:
            await self.quest4(ctx)
        elif ans.content.lower() in ansn:
            await ctx.send("not yet implemented")
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def quest4(self, ctx):
        await ctx.send("You hear the rattling sound of the generator starting. The lights come on, but suddenly you hear an ear-shattering explosion. All the lights go out and it's dark again except for the glow of your flashlight. You can hear fire in the background. Are you heading towards the fire?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        if ans.content.lower() in ansy:
            await self.quest5(ctx)
        elif ans.content.lower() in ansn:
            await ctx.send("not yet implemented")
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def quest5(self, ctx):
        await ctx.send("When you arrive at the fire, you see the destroyed airlock to the reactor core. Are you going in?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        if ans.content.lower() in ansy:
            await self.quest6(ctx)
        elif ans.content.lower() in ansn:
            await ctx.send("not yet implemented")
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def quest6(self, ctx):
        await ctx.send("Once inside you see the reactor core glowing bright red. You also see that the cooling water has almost completely drained out. You notice: You are on the verge of a meltdown. Just as you're about to despair, you see an EMERGENCY STOP button behind a shatterable pane of glass. Are you running towards it?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        if ans.content.lower() in ansy:
            await self.quest7(ctx)
        elif ans.content.lower() in ansn:
            await ctx.send("not yet implemented")
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def quest7(self, ctx):
        await ctx.send("When you have almost reached the glass, you see that between you and the button there is a chasm into the glowing hot cooling water. Do you jump over it?")
        ans = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
        ansy = await self.answer_yes()
        if ans.content.lower() in ansy:
            await self.death_by_nuclear_rod(ctx)
        elif ans.content.lower() in ansn:
            await ctx.send("not yet implemented")
        else:
            await ctx.respond("Answer not defined. Please use yes and no. Use the command again to retry.")

    async def death_by_nuclear_rod(self, ctx):
        await ctx.send("You try to jump, but you stumble and fall into the chasm. You hit the reactor rods and you get queasy...")
        await ctx.send("💀**You died**💀")

    async def death_by_gas_fire(self, ctx):
        await ctx.send("You don't think much about it and keep walking.\nFrom one moment to the other, you hear a loud woooosh and only see red flames. You realize that this was the last decision of your life as you burn to death.")
        await ctx.send("💀**You died**💀")

    @commands.slash_command(name="nuclear_fallout_ita", description="Minigame in development")
    async def nf_command(self, ctx):
        await self.quest0(ctx)

def setup(client):
    client.add_cog(nf_game(client))