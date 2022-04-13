import discord
from discord.ext import commands
import asyncio
from discord.ext import tasks
from datetime import datetime
from datetime import date
import json
from discord.ext.commands import CommandNotFound
import os
from discord.utils import get
#from antispam import AntiSpamHandler, Options
from collections import Counter
import collections
import schedule
from discord.ext.commands import MemberNotFound
import sys
import subprocess
from decouple import config
# from AntiSpamTrackerSubclass import MyCustomTracker
import re

localmuchusedbadwords = ["ass","clit","cum","coon","coons","fuck","honkey","hooker","jizz","juggs","rape","scat","semen","spic","spunk","suck","sucks","swinger","skeet","slanteye","tit","tits","tushy","twat","twink","twinkie","nipple","nipples","nude","nudity","wank","wetback","queaf","queef","quim","xx","xxx"]
localbadwords = ["2g1c","2 girls 1 cup","acrotomophilia","alabama hot pocket","alaskan pipeline","anal","anilingus","anus","apeshit","arsehole","asshole","assmunch","auto erotic","autoerotic","babeland","baby batter","baby juice","ball gag","ball gravy","ball kicking","ball licking","ball sack","ball sucking","bangbros","bareback","barely legal","barenaked","bastard","bastardo","bastinado","bbw","bdsm","beaner","beaners","beaver cleaver","beaver lips","bestiality","big black","big breasts","big knockers","big tits","bimbos","birdlock","bitch","bitches","black cock","blonde action","blonde on blonde action","blowjob","blow job","blow your load","blue waffle","blumpkin","bollocks","bondage","boner","boob","boobs","booty call","brown showers","brunette action","bukkake","bulldyke","bullet vibe","bullshit","bung hole","bunghole","busty","butt","buttcheeks","butthole","camel toe","camgirl","camslut","camwhore","carpet muncher","carpetmuncher","chocolate rosebuds","circlejerk","cleveland steamer","clitoris","clover clamps","clusterfuck","cock","cocks","coprolagnia","coprophilia","cornhole","creampie","cumming","cunnilingus","cunt","darkie","date rape","daterape","deep throat","deepthroat","dendrophilia","dick","dildo","dingleberry","dingleberries","dirty pillows","dirty sanchez","doggie style","doggiestyle","doggy style","doggystyle","dog style","dolcett","domination","dominatrix","dommes","donkey punch","double dong","double penetration","dp action","dry hump","dvda","eat my ass","ecchi","ejaculation","erotic","erotism","escort","eunuch","faggot","fecal","felch","fellatio","feltch","female squirting","femdom","figging","fingerbang","fingering","fisting","foot fetish","footjob","frotting","fuck buttons","fuckin","fucking","fucktards","fudge packer","fudgepacker","futanari","gang bang","gay sex","genitals","giant cock","girl on","girl on top","girls gone wild","goatcx","goatse","god damn","gokkun","golden shower","goodpoop","goo girl","goregasm","grope","group sex","g-spot","guro","hand job","handjob","hard core","hardcore","hentai","homoerotic","hot carl","hot chick","how to kill","how to murder","huge fat","humping","incest","intercourse","jack off","jail bait","jailbait","jelly donut","jerk off","jigaboo","jiggaboo","jiggerboo","kike","kinbaku","kinkster","kinky","knobbing","leather restraint","leather straight jacket","lemon party","lolita","lovemaking","make me come","male squirting","masturbate","menage a trois","milf","missionary position","motherfucker","mound of venus","mr hands","muff diver","muffdiving","nambla","nawashi","negro","neonazi","nigga","nigger","nig nog","nimphomania","nsfw images","nympho","nymphomania","octopussy","omorashi","one cup two girls","one guy one jar","orgasm","orgy","paedophile","paki","panties","panty","pedobear","pedophile","pegging","penis","phone sex","piece of shit","pissing","piss pig","pisspig","playboy","pleasure chest","pole smoker","ponyplay","poontang","punany","poop chute","poopchute","porn","porno","pornography","prince albert piercing","pthc","pubes","pussy","raghead","raging boner","raping","rapist","rectum","reverse cowgirl","rimjob","rimming","rosy palm","rosy palm and her 5 sisters","rusty trombone","sadism","santorum","schlong","scissoring","sex","sexo","shaved beaver","shaved pussy","shemale","shibari","shit","shitblimp","shitty","shota","shrimping","slut","s&m","smut","snatch","snowballing","sodomize","sodomy","splooge","splooge moose","spooge","spread legs","strap on","strapon","strappado","strip club","style doggy","suicide girls","sultry women","tainted love","taste my","tea bagging","threesome","throating","tied up","tight white","titties","titty","tongue in a","topless","tosser","towelhead","tranny","tribadism","tub girl","tubgirl","two girls one cup","undressing","upskirt","urethra play","urophilia","vagina","venus mound","vibrator","violet wand","vorarephilia","voyeur","vulva","wet dream","white power","wrapping men","wrinkled starfish","yaoi","yellow showers","yiffy","zoophilia","🖕"]
allowedroles = [951207540472029195, 589435378147262464, 632674518317531137]#, 951464246506565683] #botdev, moderator, admin, testserveradmin
"""HELPER NICHT WEGEN ABHOY xd"""

class messagefilter(commands.Cog):
    def __init__(self, client):
        self.client = client

    """async def get_badwords(self):
        with open("json_files/badwords.json", "r") as f:
            badwords = json.load(f)
        return badwords"""

    @commands.Cog.listener()
    async def on_message(self, message):
        if not isinstance(message.channel, discord.DMChannel):
            badwordarr = localbadwords #await self.get_badwords()
            muchusedarr =localmuchusedbadwords
            author = message.author
            webhooks = await message.channel.webhooks()
            swearword = False
            content = message.content
            replacement = ":heart:"
            explanation = "\n\nPS: ||I said something naughty, so the wonderfully nice bot replaced everything with love...||"
            if not message.author.bot:
                if any(role.id in allowedroles for role in author.roles):
                    return
                for badword in badwordarr:
                    if badword.lower() in content.lower():
                        compiled = re.compile(re.escape(badword.lower()), re.IGNORECASE)
                        content = compiled.sub(replacement, content)
                        swearword = True
                for badword in muchusedarr:
                    badword2 = badword + " "
                    badword3 = badword
                    badword4 = " " + badword
                    badword = " " + badword + " "
                    if badword.lower() in content.lower():
                        compiled = re.compile(re.escape(badword.lower()), re.IGNORECASE)
                        content = compiled.sub(replacement, content)
                        swearword = True
                    if content.lower().startswith(badword2.lower()):
                        compiled = re.compile(re.escape(badword2.lower()), re.IGNORECASE)
                        content = compiled.sub(replacement, content)
                        swearword = True
                    if content.lower() == badword3.lower():
                        compiled = re.compile(re.escape(badword3.lower()), re.IGNORECASE)
                        content = compiled.sub(replacement, content)
                        swearword = True
                    if content.lower()[-len(badword4):] == badword4:
                        compiled = re.compile(re.escape(badword4.lower()), re.IGNORECASE)
                        content = compiled.sub(replacement, content)
                        swearword = True
                if swearword == True:
                    await message.delete()
                    if len(content) > 1000:
                        content = content[:1000]
                    content = content + explanation
                    if webhooks:
                        for webhook in webhooks:
                            await webhook.send(content=content, username=author.name, avatar_url=author.avatar.url)
                            break
                    elif not webhooks:
                        webhook = await message.channel.create_webhook(name="BadWordHook")
                        await webhook.send(content=content, username=author.name, avatar_url=author.avatar.url)

def setup(client):
	client.add_cog(messagefilter(client))