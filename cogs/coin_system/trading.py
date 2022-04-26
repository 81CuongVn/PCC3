import charset_normalizer
from discord.ext import commands
import discord
from discord import Option
import json
from discord.ui import View, Select
from bank_functions import get_bank_data


class trading(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="trading", description="Trade parts", guild_ids=[951463924279181322])
    async def trading_slash(self, ctx, trading_partner : Option(discord.Member, required=True), what_you_give: Option(str, choices=['Part(s)', 'Money'], required=True), what_you_want: Option(str, choices=['Part(s)', 'Money'], required=True)):
        await self.new_trading_member(ctx.author)
        await self.new_trading_member(trading_partner)
        trading_member = await self.get_trading()
        trading_list = await self.get_trading_list()

        

        if what_you_give == "Part(s)":

            with open("json_files/useritems.json", "r") as f:
                useritems = json.load(f)

            if str(ctx.author.id) in useritems:    

                items = useritems[str(ctx.author.id)]   
                i = 0
                u = 0
                items_shown = []
                items_list = []

                while u<len(items):
                    if items[u] in items_shown:
                        pass
                    else:
                        items_shown.append(items[u])
                    u += 1     

                while i<len(items_shown):
                    items_list.append(discord.SelectOption(label=items_shown[i]))
                    i += 1

                item_select = Select(placeholder="Choose an option", min_values=1, max_values=i, options=items_list)

                view = View()
                view.add_item(item_select)

                await ctx.respond("Choose the part you want to sell.", view=view)

            else:
                await ctx.respond("You don't have any items.")
                return


        if what_you_give == "Money":
            bank_account = await get_bank_data()
            if str(ctx.author.id) in bank_account:  
                money_you_have = bank_account[str(ctx.author.id)]["money"]
                await ctx.respond(f"You have {money_you_have}<:bot_icon:951868023503986699>\nHow much money do you want to pay?")
                global ans1
                ans1 = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                ans1 = ans1.content
                try:
                    ans1 = int(ans1)
                except:
                    await ctx.send("You can't use letters or numbers with a ,.")
                    return
                await ctx.send(f"You will pay {ans1}<:bot_icon:951868023503986699>.")
                

                if what_you_want == "Money":
                    if str(trading_partner.id) in bank_account: 
                        money_you_have = bank_account[str(trading_partner.id)]["money"]
                        await ctx.send(f"Your partner has {money_you_have}<:bot_icon:951868023503986699>.\nHow much money do you want to get?")
                        global ans2
                        ans2 = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                        ans2 = ans2.content
                        try:
                            ans2 = int(ans2)
                        except:
                            await ctx.send("You can't use letters or numbers with a ,.")
                            return
                        await ctx.send(f"You will get {ans2}<:bot_icon:951868023503986699>") 
                        old_trading_count = trading_list["trading_count"]
                        new_trading_count = old_trading_count + 1
                        trading_list["trading_count"] = new_trading_count
                        trading_list[f"trade_{new_trading_count}"] = {}
                        trading_list[f"trade_{new_trading_count}"]["give_type"] = "coins"
                        trading_list[f"trade_{new_trading_count}"]["give_coins_amt"] = ans1
                        trading_list[f"trade_{new_trading_count}"]["want_type"] = "coins"
                        trading_list[f"trade_{new_trading_count}"]["want_coins_amount"] = ans2
                        trading_list[f"trade_{new_trading_count}"]["trade_guy_1"] = str(ctx.author.id)
                        trading_list[f"trade_{new_trading_count}"]["trade_guy_2"] = str(trading_partner.id)
                        trading_author_list = trading_member[str(ctx.author.id)]
                        trading_partner_list = trading_member[str(trading_partner.id)]
                        trading_author_list.append(new_trading_count)
                        trading_partner_list.append(new_trading_count)
                        with open("json_files/trading_list.json", "w") as f:
                            json.dump(trading_list,f)
                        with open("json_files/trading_member.json", "w") as f:
                            json.dump(trading_member,f)
                        return
                    else:
                        await ctx.send("Your trading partner does not have a bank account.")
                        return    

                if what_you_want == "Part(s)":
                    with open("json_files/useritems.json", "r") as f:
                        useritems = json.load(f)
                    if str(ctx.author.id) in useritems:
                        items_partner = useritems[str(trading_partner.id)]   
                        j = 0            
                        h = 0
                        items_list_partner = []
                        items_shown_partner = []

                        while j<len(items_partner):
                            if items_partner[j] in items_shown_partner:
                                pass
                            else:
                                items_shown_partner.append(items_partner[j])
                            j += 1     

                        while h<len(items_shown_partner):
                            items_list_partner.append(discord.SelectOption(label=items_shown_partner[h]))
                            h += 1

                        item_select_partner2 = Select(placeholder="Choose an option", min_values=1, max_values=h, options=items_list_partner)
                        partner_choose_part = View()
                        partner_choose_part.add_item(item_select_partner2)

                        await ctx.send("Choose an item you want to buy.", view=partner_choose_part)      
                    else:
                        await ctx.send("Your trading partner has no items.")
                        return                 
                    
            else:
                await ctx.respond("Use `/create_bank_account` to create a bank account.", ephemeral=True)
                #trading[str(ctx.author.id)]["trade_counter"]
                return   

        #global item_select_callback
        async def item_select_partner2_callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await ctx.send(f"<@{interaction.user.id}> you can't do that.")
                return True

            #print("OK")

            if what_you_want == "Money":
                pass

            if what_you_give == "Part(s)":
                give_type = "parts"

            if what_you_give == "Money":
                give_type = "coins"    

            if what_you_want == "Part(s)":

                item_you_want = item_select_partner2.values
                every_item_you_want = ", ".join(item_you_want)
                await interaction.message.edit(f"You want to buy **{every_item_you_want}**", view=None) 

                old_trading_count = trading_list["trading_count"]
                new_trading_count = old_trading_count + 1
                trading_list["trading_count"] = new_trading_count
                trading_list[f"trade_{new_trading_count}"] = {}
                trading_list[f"trade_{new_trading_count}"]["give_type"] = give_type
                if what_you_give == "Part(s)":
                    trading_list[f"trade_{new_trading_count}"]["give_item"] = item_you_give
                if what_you_give == "Money":   
                    trading_list[f"trade_{new_trading_count}"]["give_coins_amt"] = ans1
                trading_list[f"trade_{new_trading_count}"]["want_type"] = "parts"
                trading_list[f"trade_{new_trading_count}"]["want_item"] = item_you_want
                trading_list[f"trade_{new_trading_count}"]["trade_guy_1"] = str(ctx.author.id)
                trading_list[f"trade_{new_trading_count}"]["trade_guy_2"] = str(trading_partner.id)
                trading_author_list = trading_member[str(ctx.author.id)]
                trading_partner_list = trading_member[str(trading_partner.id)]
                trading_author_list.append(new_trading_count)
                trading_partner_list.append(new_trading_count)
                with open("json_files/trading_list.json", "w") as f:
                    json.dump(trading_list,f)
                with open("json_files/trading_member.json", "w") as f:
                    json.dump(trading_member,f)
                return         

        async def item_select_callback(interaction:discord.Interaction):
            if interaction.user != ctx.author:
                await ctx.send(f"<@{interaction.user.id}> you can't do that.")
                return True

            if what_you_give == "Part(s)":
                global item_you_give
                item_you_give = item_select.values
                every_item_you_give = ", ".join(item_you_give)
                await interaction.message.edit(content=f"You want to sell **{every_item_you_give}**.", view=None)

            if what_you_want == "Part(s)":

                with open("json_files/useritems.json", "r") as f:
                    useritems = json.load(f)

                items_partner = useritems[str(trading_partner.id)]   
                k = 0
                l = 0
                items_list_partner = []
                items_shown_partner = []

                while k<len(items_partner):
                    if items_partner[k] in items_shown_partner:
                        pass
                    else:
                        items_shown_partner.append(items_partner[k])
                        k += 1        

                while l<len(items_shown_partner):
                    items_list_partner.append(discord.SelectOption(label=items_shown_partner[l]))
                    l += 1

                item_select_partner = Select(placeholder="Choose an option", min_values=1, max_values=l, options=items_list_partner)

                partner_choose_part = View()
                partner_choose_part.add_item(item_select_partner)

                await interaction.message.channel.send("Choose the item you want to buy.", view=partner_choose_part)


            if what_you_want == "Money":
                bank_account = await get_bank_data()
                if str(trading_partner.id) in bank_account: 
                    money_you_have = bank_account[str(trading_partner.id)]["money"]
                    await interaction.response.send_message(f"Your partner has {money_you_have}<:bot_icon:951868023503986699>\nHow much money do you want to get?")
                    global ans3
                    ans3 = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                    ans3 = ans3.content
                    try:
                        ans3 = int(ans3)
                    except:
                        await interaction.message.channel.send("You can't use letters or numbers with a ,.")
                        return True   
                    if ans3 == ans3:    
                        await ctx.send(f"You want to get {ans3}<:bot_icon:951868023503986699>.")
                        old_trading_count = trading_list["trading_count"]
                        new_trading_count = old_trading_count + 1
                        trading_list["trading_count"] = new_trading_count
                        trading_list[f"trade_{new_trading_count}"] = {}
                        trading_list[f"trade_{new_trading_count}"]["give_type"] = "parts"
                        trading_list[f"trade_{new_trading_count}"]["give_item"] = item_you_give
                        trading_list[f"trade_{new_trading_count}"]["want_type"] = "coins"
                        trading_list[f"trade_{new_trading_count}"]["want_coins_amount"] = ans3
                        trading_list[f"trade_{new_trading_count}"]["trade_guy_1"] = str(ctx.author.id)
                        trading_list[f"trade_{new_trading_count}"]["trade_guy_2"] = str(trading_partner.id)
                        trading_author_list = trading_member[str(ctx.author.id)]
                        trading_partner_list = trading_member[str(trading_partner.id)]
                        trading_author_list.append(new_trading_count)
                        trading_partner_list.append(new_trading_count)
                        with open("json_files/trading_list.json", "w") as f:
                            json.dump(trading_list,f)
                        with open("json_files/trading_member.json", "w") as f:
                            json.dump(trading_member,f)
                        return True
                    else:
                        await interaction.message.channel.send("An error occured")
                        return True
                else:
                    await interaction.message.channel.send("Your trading partner doesn not have a bank account.")
                    return True
                           


            async def item_select_partner_callback(interaction:discord.Interaction):
                if interaction.user != ctx.author:
                    await ctx.send(f"<@{interaction.user.id}> you cant do that")
                    return True

                #print("OK")

                if what_you_want == "Money":
                    pass

                if what_you_give == "Part(s)":
                    give_type = "parts"

                if what_you_give == "Money":
                    give_type = "coins"    

                if what_you_want == "Part(s)":

                    item_you_want = item_select_partner.values
                    every_item_you_want = ", ".join(item_you_want)
                    await interaction.message.edit(f"You want to buy **{every_item_you_want}**", view=None) 

                    old_trading_count = trading_list["trading_count"]
                    new_trading_count = old_trading_count + 1
                    trading_list["trading_count"] = new_trading_count
                    trading_list[f"trade_{new_trading_count}"] = {}
                    trading_list[f"trade_{new_trading_count}"]["give_type"] = give_type
                    if what_you_give == "Part(s)":
                        trading_list[f"trade_{new_trading_count}"]["give_item"] = item_you_give
                    if what_you_give == "Money":   
                        trading_list[f"trade_{new_trading_count}"]["give_coins_amt"] = ans1
                    trading_list[f"trade_{new_trading_count}"]["want_type"] = "parts"
                    trading_list[f"trade_{new_trading_count}"]["want_item"] = item_you_want
                    trading_list[f"trade_{new_trading_count}"]["trade_guy_1"] = str(ctx.author.id)
                    trading_list[f"trade_{new_trading_count}"]["trade_guy_2"] = str(trading_partner.id)
                    trading_author_list = trading_member[str(ctx.author.id)]
                    trading_partner_list = trading_member[str(trading_partner.id)]
                    trading_author_list.append(new_trading_count)
                    trading_partner_list.append(new_trading_count)
                    with open("json_files/trading_list.json", "w") as f:
                        json.dump(trading_list,f)
                    with open("json_files/trading_member.json", "w") as f:
                        json.dump(trading_member,f)
                    return

            item_select_partner.callback = item_select_partner_callback  

        item_select_partner2.callback = item_select_partner2_callback
        item_select.callback = item_select_callback   



    async def get_trading_list(self):
        with open("json_files/trading_list.json", "r") as f:
            trading_list = json.load(f)
        return trading_list
        
    async def get_trading(self):
        with open("json_files/trading_member.json", "r") as f:
            trading = json.load(f)
        return trading

    async def new_trading_member(self, member):
        trading = await self.get_trading()

        if str(member.id) in trading:
            return False
        else:
            trading[str(member.id)] = []
    
        with open("json_files/trading_member.json", "w") as f:
            json.dump(trading,f)
        return True


def setup(client):
    client.add_cog(trading(client))    