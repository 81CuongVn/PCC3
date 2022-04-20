#from dis import disco
import discord
from discord.ext import commands
import random
from discord.ui import Button, View
import json
from bank_functions import new_member, get_coins, update_bank
from discord import Option

async def button_function(button_number,interaction):
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[4][button_number-1]==":white_large_square:":
              if ttt_list_2[0] == interaction.user.id:
                ttt_list_2[4][button_number-1] = ":regional_indicator_x:"
                mark = ":regional_indicator_x:"
              else:
                ttt_list_2[4][button_number-1] = ":o2:"
                mark = ":o2:"
              gameOver = False
              send = interaction.response.send_message
              return_list = []
              gameOver=False
              x=0
              y=0
              ttt_list_update = ttt_list_2[4]
              for i in range(9):
                if ttt_list_update[x] == ":white_large_square:":
                  return_list.append("⬜")
                elif ttt_list_update[x] == ":regional_indicator_x:":
                  return_list.append("❎")
                  y+=1
                elif ttt_list_update[x] == ":o2:":
                  return_list.append("🅾")
                  y+=1
                x+=1
              winningConditions_1 = [
                [0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]
              ]

              game_list = return_list

              for condition in winningConditions_1:
                if ttt_list_update[condition[0]] == mark and ttt_list_update[condition[1]] == mark and ttt_list_update[condition[2]] == mark:
                  gameOver = True
              
              if gameOver == True:
                await interaction.message.edit(f"<@{interaction.user.id}> won and got the entire money.",view=None)
                await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
              elif y == 9:
                await update_bank(ttt_list_2[0], send, ttt_list_2[5], mode = "wallet")
                await update_bank(ttt_list_2[1], send, ttt_list_2[5], mode = "wallet")
                await interaction.response.send_message(content="It's a tie\nBoth of you got your entry money back")
              else:
                if ttt_list_2[3] == ttt_list_2[0]:
                  ttt_list_2[3] = ttt_list_2[1]
                else:
                  ttt_list_2[3] = ttt_list_2[0]
                await interaction.message.edit(f"It was <@{interaction.user.id}>'s turn. Now it's your turn <@{ttt_list_2[3]}>.\n{game_list[0]}{game_list[1]}{game_list[2]}\n{game_list[3]}{game_list[4]}{game_list[5]}\n{game_list[6]}{game_list[7]}{game_list[8]}")
            else:
              await interaction.response("This field is occupied")
          else:
            await interaction.response.send_message("It is not your turn <@{interaction.user.id}>.")

class PersistentView(discord.ui.View):
    def __init__(self):
      super().__init__(timeout=None)

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="1", row=1,custom_id="persistent_view:button_ttt_1_callback")
    async def button_ttt_1_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      await button_function(1,interaction)

    #@discord.ui.Button(style=discord.ButtonStyle.primary, label="Give up", row=4,custom_id=)
    @discord.ui.button(style=discord.ButtonStyle.secondary, label="2", row=1,custom_id="persistent_view:button_ttt_2_callback")
    async def button_ttt_2_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      await button_function(2,interaction)

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="3", row=1,custom_id="persistent_view:button_ttt_3_callback")
    async def button_ttt_3_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      await button_function(3,interaction)

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="4", row=2,custom_id="persistent_view:button_ttt_4_callback")
    async def button_ttt_4_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      await button_function(4,interaction)

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="5", row=2,custom_id="persistent_view:button_ttt_5_callback")
    async def button_ttt_5_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      await button_function(5,interaction)

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="6", row=2,custom_id="persistent_view:button_ttt_6_callback")
    async def button_ttt_6_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      await button_function(6,interaction)

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="7", row=3,custom_id="persistent_view:button_ttt_7_callback")
    async def button_ttt_7_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      await button_function(7,interaction)

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="8", row=3,custom_id="persistent_view:button_ttt_8_callback")
    async def button_ttt_8_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      await button_function(8,interaction)

    @discord.ui.button(style=discord.ButtonStyle.secondary, label="9", row=3,custom_id="persistent_view:button_ttt_9_callback")
    async def button_ttt_9_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      await button_function(9,interaction)

    @discord.ui.button(style=discord.ButtonStyle.danger,label="give up",row=4,custom_id="persistent_view:button_ttt_give_up")
    async def button_ttt_give_up(self, button:discord.ui.button,interaction:discord.Interaction):
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id:
          if ttt_list_2[0] == interaction.user.id:
            send = interaction.response.send_message
            await interaction.message.edit(f"<@{ttt_list_2[0]}> gave up and let <@{ttt_list_2[1]}> get got the money.",view=None)
            await update_bank(ttt_list_2[1], send, 2*ttt_list_2[5], mode = "wallet")
          elif ttt_list_2[1] == interaction.user.id:
            send = interaction.response.send_message
            await interaction.message.edit(f"<@{ttt_list_2[1]}> gave up and let <@{ttt_list_2[0]}> get the money.",view=None)
            await update_bank(ttt_list_2[0], send, 2*ttt_list_2[5], mode = "wallet")

class PersistentViewBot(commands.Bot):
    def __init__(self):
        super().__init__()
        self.persistent_views_added = False

    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(PersistentView())
            self.persistent_views_added = True


class tictactoe_buttons(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    global board
    board = []
    winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    global new_games
    new_games = []


    @commands.slash_command(name="tic_tac_toe")
    async def tictactoe_buttons(self, ctx, opponent: Option(discord.Member, required=True), amount: Option(int, required=True)):
        global player1
        global player2
        global turn
        global gameOver
        global p1
        global p2_2
        global amount_2
        global new_games

        p2 = opponent
        member = ctx.author      
        await new_member(member)
        user = member
        users_coins = await get_coins()
        coins_amt_str = users_coins[str(user.id)]
        coins_amt = int(coins_amt_str)

        if amount > coins_amt:
            await ctx.respond(f"You dont have that much money (You have {coins_amt}<:bot_icon:951868023503986699>)")
            return
        if amount <= 0:
          await ctx.respond(f"You can't use {amount}<:bot_icon:951868023503986699>. Use more than 0")
          return
        amount_2 = amount
        player1 = ""
        player2 = ""
        turn = ""
        gameOver = True

        p1 = ctx.author

        if p2 == ctx.author or p2.bot:
                await ctx.respond("You can't play against yourself or a Bot.")
                return
        p2_2 = p2

        button_p2_accept = Button(style=discord.ButtonStyle.green, label="accept")
        button_p2_declince = Button(style=discord.ButtonStyle.red, label="declince")
        view = View()
        view.add_item(button_p2_accept)
        view.add_item(button_p2_declince)
        start_message = await ctx.send(f"<@{p2.id}>, press the green button below this message to accept the invite to this tic-tac-toe game. You will have to pay {amount}<:bot_icon:951868023503986699> to enter. You can decline by pressing the red button.", view=view)

        new_games.append([
          ctx.author.id,
          p2.id,
          amount,
          start_message.id
        ])

        async def button_p2_accept_callback(interaction):
          global new_games
          for game_start in new_games:
            if game_start[3] == interaction.message.id:
              if interaction.user.id == game_start[1]:
                member = interaction.user      
                await new_member(member)
                user = member
                users_coins = await get_coins()
                coins_amt_str = users_coins[str(user.id)]
                coins_amt = int(coins_amt_str)

                if game_start[2] > coins_amt:
                      await ctx.send(f"You dont have that much money (You have {coins_amt}<:bot_icon:951868023503986699>)")
                      return
                else:
                      await interaction.response.edit_message(content="The game started:", view=None)
                      new_games.remove(game_start)
                      global gameOver
                      send = ctx.respond
                      await update_bank(p1, send, -1*amount, mode = "wallet")
                      await update_bank(p2_2, send, -1*amount, mode = "wallet")
                      if bool(gameOver):
                          global board

                          p3_1 = random.randint(1,2)
                          if p3_1 == 1:
                            p3 = p1
                          elif p3_1 == 2:
                            p3 = p2
                          ttt_start_msg = await ctx.send(f"<@{p1.id}> vs <@{p2_2.id}>\nIt's <@{p3.id}> turn.\n⬜⬜⬜\n⬜⬜⬜\n⬜⬜⬜",view=PersistentView())
                          whois_turn = p3
                          board.append([
                              p1.id,
                              p2_2.id,
                              ttt_start_msg.id,
                              whois_turn.id,
                              [":white_large_square:", ":white_large_square:", ":white_large_square:",
                              ":white_large_square:", ":white_large_square:", ":white_large_square:",
                              ":white_large_square:", ":white_large_square:", ":white_large_square:"],
                              amount
                          ])

        async def button_p2_declince_callback(interaction):
          global new_games
          for game_start in new_games:
            if game_start[3] == interaction.message.id:
              if interaction.user != game_start[1]:
                await  interaction.respond(f"<@{interaction.user.id}>, you can't use this. Go start your own game.")
                return
              else:
                await interaction.response.edit_message(content=f"{p2_2} declined the offer.", view=None)
                new_games.remove(game_start)



        #button_ttt_give_up.callback = button_ttt_give_up_callback
        button_p2_declince.callback = button_p2_declince_callback


        button_p2_accept.callback = button_p2_accept_callback


def setup(client):
    client.add_cog(tictactoe_buttons(client))