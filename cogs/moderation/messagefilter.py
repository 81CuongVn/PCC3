
import discord
from discord.ext import commands
import json
import re

with open("json_files/mainconfig.json", encoding="utf-8-sig") as f:
    mainconfig = json.load(f)

localmuchusedbadwords = ["ass","clit","cum","coon","coons","honkey","hooker","fuck","jizz","juggs","rape","scat","semen","spic","spunk","suck","sucks","swinger","skeet","slanteye","tit","tits","tushy","twat","twink","twinkie","nipple","nipples","nude","nudity","wank","wetback","queaf","queef","quim","xx","xxx","fuckin","fucking","shit","shitty","bbw","bdsm","dick","erotic","erotism","escort","cunt","cock","kike","dommes","faggot","pissing","penis","playboy","milf","pthc","pubes","pussy","humping","incest","nambla","nawashi","neonazi","nigga","nigger","raping","rapist","rectum","fecal","felch","fellatio","feltch","paki","panties","panty","orgy","slut","s&m","smut","snatch","sadism","santorum","schlong","scissoring","strap on","strapon","titties","titty","sex","sexo","busty","butt","yiffy","nigg","nig"]
localbadwords = ["2g1c","2 girls 1 cup","acrotomophilia","motherfuck","alabama hot pocket","alaskan pipeline","anal","anilingus","anus","apeshit","arsehole","asshole","assmunch","auto erotic","autoerotic","babeland","baby batter","baby juice","ball gag","ball gravy","ball kicking","ball licking","ball sack","ball sucking","bangbros","bareback","barely legal","barenaked","bastard","bastardo","bastinado","beaner","beaners","beaver cleaver","beaver lips","bestiality","big black","big breasts","big knockers","big tits","bimbos","birdlock","bitch","bitches","black cock","blonde action","blonde on blonde action","blowjob","blow job","blow your load","blue waffle","blumpkin","bollocks","bondage","boner","boob","boobs","booty call","brown showers","brunette action","bukkake","bulldyke","bullet vibe","bullshit","bung hole","nigger","nigga","bunghole","buttcheeks","butthole","camel toe","camgirl","camslut","camwhore","carpet muncher","carpetmuncher","chocolate rosebuds","circlejerk","cleveland steamer","clitoris","clover clamps","clusterfuck","cocks","coprolagnia","coprophilia","cornhole","creampie","cumming","cunnilingus","darkie","date rape","daterape","deep throat","deepthroat","dendrophilia","dildo","dingleberry","dingleberries","dirty pillows","dirty sanchez","doggie style","doggiestyle","doggy style","doggystyle","dog style","dolcett","domination","dominatrix","donkey punch","double dong","double penetration","dp action","dry hump","dvda","eat my ass","ecchi","ejaculation","eunuch","female squirting","femdom","figging","fingerbang","fingering","fisting","foot fetish","footjob","frotting","fuck buttons","fucktards","fudge packer","fudgepacker","futanari","gang bang","gay sex","genitals","giant cock","girl on","girl on top","girls gone wild","goatcx","goatse","god damn","gokkun","golden shower","goodpoop","goo girl","goregasm","grope","group sex","g-spot","guro","hand job","handjob","hard core","hardcore","hentai","homoerotic","hot carl","hot chick","how to kill","how to murder","huge fat","intercourse","jack off","jail bait","jailbait","jelly donut","jerk off","jigaboo","jiggaboo","jiggerboo","kinbaku","kinkster","kinky","knobbing","leather restraint","leather straight jacket","lemon party","lolita","lovemaking","make me come","male squirting","masturbate","menage a trois","missionary position","motherfucker","mound of venus","mr hands","muff diver","muffdiving","nig nog","nimphomania","nsfw images","nympho","nymphomania","octopussy","omorashi","one cup two girls","one guy one jar","orgasm","paedophile","pedobear","pedophile","pegging","phone sex","piece of shit","piss pig","pisspig","pleasure chest","pole smoker","ponyplay","poontang","punany","poop chute","poopchute","porn","porno","pornography","prince albert piercing","raghead","raging boner","reverse cowgirl","rimjob","rimming","rosy palm","rosy palm and her 5 sisters","rusty trombone","shaved beaver","shaved pussy","shemale","shibari","shitblimp","shota","shrimping","snowballing","sodomize","sodomy","splooge","splooge moose","spooge","spread legs","strappado","strip club","style doggy","suicide girls","sultry women","tainted love","taste my","tea bagging","threesome","throating","tight white","tongue in a","topless","tosser","towelhead","tranny","tribadism","tub girl","tubgirl","two girls one cup","undressing","upskirt","urethra play","urophilia","vagina","venus mound","vibrator","violet wand","vorarephilia","voyeur","vulva","wet dream","white power","wrapping men","wrinkled starfish","yaoi","yellow showers","zoophilia"]
allowedroles = mainconfig["allowed_filter"] #[951207540472029195, 589435378147262464, 632674518317531137] #, 951464246506565683] #botdev, moderator, admin, testserveradmin

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
            await self.checkfornaughtyword(message)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not isinstance(before.channel, discord.DMChannel):
            await self.checkfornaughtyword(after)
    
    async def checkfornaughtyword(self, message):
        if message != None:
            if not message.author.bot:
                badwordarr = localbadwords #await self.get_badwords()
                muchusedarr =localmuchusedbadwords #await self.get_muchusedbadwords()
                author = message.author
                try:
                    webhooks = await message.channel.webhooks()
                except:
                    webhooks = None
                swearword = False
                content = message.content
                #replacement = ":heart:"
                explanation = "\n\nPlease stop using swear words (rule 5).\nYou can read the rules in <#605326085328207872>.​"
                if any(role.id in allowedroles for role in author.roles):
                    return
                #nospacecontent = content.replace(" ", "")
                for badword in badwordarr:
                    if badword.lower() in content.lower():
                        compiled = re.compile(re.escape(badword.lower()), re.IGNORECASE)
                        lengthofbadword = len(badword) - 1
                        replacement = '٭' * lengthofbadword
                        replacement = badword[0] + replacement
                        content = compiled.sub(replacement, content)
                        swearword = True
                for badword in muchusedarr:
                    badword2 = badword + " "
                    badword3 = badword
                    badword4 = " " + badword
                    badword = " " + badword + " "
                    if badword.lower() in content.lower():
                        lengthofbadword = len(badword3) - 1
                        replacement = '٭' * lengthofbadword
                        replacement = badword3[0] + replacement
                        compiled = re.compile(re.escape(badword3.lower()), re.IGNORECASE)
                        content = compiled.sub(replacement, content)
                        swearword = True
                    if content.lower().startswith(badword2.lower()):
                        lengthofbadword = len(badword3) - 1
                        replacement = '٭' * lengthofbadword
                        replacement = badword3[0] + replacement
                        compiled = re.compile(re.escape(badword3.lower()), re.IGNORECASE)
                        content = compiled.sub(replacement, content)
                        swearword = True
                    if content.lower() == badword3.lower():
                        lengthofbadword = len(badword3) - 1
                        replacement = '٭' * lengthofbadword
                        replacement = badword3[0] + replacement
                        compiled = re.compile(re.escape(badword3.lower()), re.IGNORECASE)
                        content = compiled.sub(replacement, content)
                        swearword = True
                    if content.lower().endswith(badword4.lower()):
                        lengthofbadword = len(badword3) - 1
                        replacement = '٭' * lengthofbadword
                        replacement = badword3[0] + replacement
                        compiled = re.compile(re.escape(badword3.lower()), re.IGNORECASE)
                        content = compiled.sub(replacement, content)
                        swearword = True
                if swearword == True:
                    #print(replacement)
                    await message.delete()
                    if len(content) > 1000:
                        content = content[:1000]
                    content = content + explanation
                    if webhooks != None:
                        if webhooks:
                            for webhook in webhooks:
                                await webhook.send(content=content, username=author.display_name, avatar_url=author.avatar.url)
                                break
                        elif not webhooks:
                            webhook = await message.channel.create_webhook(name="BadWordHook")
                            await webhook.send(content=content, username=author.display_name, avatar_url=author.avatar.url)
                        return True
                    else:
                        return True
                return True
            return False

def setup(client):
	client.add_cog(messagefilter(client))