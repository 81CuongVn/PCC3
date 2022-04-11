
from datetime import datetime, timedelta
from platform import architecture, python_version
from time import time
import cpuinfo
from discord import Embed, client
from discord.ext import commands
from psutil import Process, virtual_memory, cpu_percent
from discord import __version__ as discord_version


class botinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="botinfo")
    async def show_bot_stats(self, ctx):
        embed = Embed(title="Bot info", colour=ctx.author.colour, timestamp=datetime.now())
        embed.set_thumbnail(url=self.client.user.avatar)

        proc = Process()
        with proc.oneshot():
            uptime = timedelta(seconds=time()-proc.create_time())
            cpu_time = timedelta(seconds=(cpu := proc.cpu_times()).system + cpu.user)
            mem_total = virtual_memory().total / (1024**2)
            mem_of_total = proc.memory_percent()
            mem_usage = mem_total * (mem_of_total / 100)
            #mem_usage = int(str(mem_usage).split(".")[0]) same Value???
            processor = cpuinfo.get_cpu_info()['brand_raw']
            cpuusage = cpu_percent()
            #cputype = cpuinfo.arch

        fields = [
            ("Bot version:", "1.7.10-pre2", True),
            ("Python version:", python_version(), True),
            ("Discord-API version:", discord_version, False),
            ("Uptime:", uptime, False),
            ("CPU name:", processor, False),
            ("CPU usage:", f"{cpuusage}%", True),
            ("CPU time:", cpu_time, True),
            ("Memory usage", f"{mem_usage:,.3f} MiB / {mem_total:,.0f} MiB ({mem_of_total:.0f}%):", False),
            ("Release-Github-Repo:", "https://github.com/YES-German/PC_Creator_2", False),
            ("Testing-Github-Repo:", "https://github.com/SleepyYui/PCC3", False),
        ]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(botinfo(bot))