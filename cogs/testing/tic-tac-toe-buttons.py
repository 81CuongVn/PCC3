import discord
from discord.ext import commands
import random
from discord.ui import Button, View
import json
from bank_functions import new_member, get_coins, update_bank
from discord import Emoji, Option

game_list = [["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],[False,False,False,False,False,False,False,False,False]]

def checkWinner(mark, board_check,gameover):
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
          for condition in winningConditions_1:
            if board_check[condition[0]] == mark and board_check[condition[1]] == mark and board_check[condition[2]] == mark:
                gameOver = False
                return gameOver

def button_update(ttt_list_update, return_list):
  if ttt_list_update[0] == ":white_large_square:":
    return_list[0].append("⬜")
    return_list[1].append(False)
  elif ttt_list_update[0] == ":regional_indicator_x:":
    return_list[0].append("❎")
    return_list[1].append(True)
  elif ttt_list_update[0] == ":o2:":
    return_list[0].append("🅾")
    return_list[1].append(True)
  if ttt_list_update[1] == ":white_large_square:":
    return_list[0].append("⬜")
    return_list[1].append(False)
  elif ttt_list_update[1] == ":regional_indicator_x:":
    return_list[0].append("❎")
    return_list[1].append(True)
  elif ttt_list_update[1] == ":o2:":
    return_list[0].append("🅾")
    return_list[1].append(True)
  if ttt_list_update[2] == ":white_large_square:":
    return_list[0].append("⬜")
    return_list[1].append(False)
  elif ttt_list_update[2] == ":regional_indicator_x:":
    return_list[0].append("❎")
    return_list[1].append(True)
  elif ttt_list_update[2] == ":o2:":
    return_list[0].append("🅾")
    return_list[1].append(True)
  if ttt_list_update[3] == ":white_large_square:":
    return_list[0].append("⬜")
    return_list[1].append(False)
  elif ttt_list_update[3] == ":regional_indicator_x:":
    return_list[0].append("❎")
    return_list[1].append(True)
  elif ttt_list_update[3] == ":o2:":
    return_list[0].append("🅾")
    return_list[1].append(True)
  if ttt_list_update[4] == ":white_large_square:":
    return_list[0].append("⬜")
    return_list[1].append(False)
  elif ttt_list_update[4] == ":regional_indicator_x:":
    return_list[0].append("❎")
    return_list[1].append(True)
  elif ttt_list_update[4] == ":o2:":
    return_list[0].append("🅾")
    return_list[1].append(True)
  if ttt_list_update[5] == ":white_large_square:":
    return_list[0].append("⬜")
    return_list[1].append(False)
  elif ttt_list_update[5] == ":regional_indicator_x:":
    return_list[0].append("❎")
    return_list[1].append(True)
  elif ttt_list_update[5] == ":o2:":
    return_list[0].append("🅾")
    return_list[1].append(True)
  if ttt_list_update[6] == ":white_large_square:":
    return_list[0].append("⬜")
    return_list[1].append(False)
  elif ttt_list_update[6] == ":regional_indicator_x:":
    return_list[0].append("❎")
    return_list[1].append(True)
  elif ttt_list_update[6] == ":o2:":
    return_list[0].append("🅾")
    return_list[1].append(True)
  if ttt_list_update[7] == ":white_large_square:":
    return_list[0].append("⬜")
    return_list[1].append(False)
  elif ttt_list_update[7] == ":regional_indicator_x:":
    return_list[0].append("❎")
    return_list[1].append(True)
  elif ttt_list_update[7] == ":o2:":
    return_list[0].append("🅾")
    return_list[1].append(True)
  if ttt_list_update[8] == ":white_large_square:":
    return_list[0].append("⬜")
    return_list[1].append(False)
  elif ttt_list_update[8] == ":regional_indicator_x:":
    return_list[0].append("❎")
    return_list[1].append(True)
  elif ttt_list_update[8] == ":o2:":
    return_list[0].append("🅾")
    return_list[1].append(True)
  return return_list

class PersistentView(discord.ui.View):
    def __init__(self):
      super().__init__(timeout=None)

    game_list=[["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],[False,False,False,False,False,False,False,False,False]]

    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji=game_list[0][0], row=1,custom_id="persistent_view:button_ttt_1_callback", disabled=game_list[1][0])
    

    async def button_ttt_1_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      global mark
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[0] == interaction.user.id:
              ttt_list_2[4][0] = ":regional_indicator_x:"
              mark = ":regional_indicator_x:"
            else:
              ttt_list_2[4][0] = ":o2:"
              mark = ":o2:"
            gameOver = False
            view_ttt=None
            send = interaction.response.send_message
            if checkWinner(mark, ttt_list_2[4],gameOver) == False:
              interaction.respond(f"<@{interaction.author.id}> win and get the entire money.")
              await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
            else:
              if ttt_list_2[3] == ttt_list_2[0]:
                ttt_list_2[3] = ttt_list_2[1]
              else:
                ttt_list_2[3] = ttt_list_2[0]
              return_list = [[],[]]
              PersistentView.game_list = button_update(ttt_list_2[4], return_list)
              await interaction.message.edit(f"It was <@{interaction.user.id}> turn so now it's <@{ttt_list_2[3]}> turn.", view=PersistentView())
              PersistentView.game_list = [["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],[False,False,False,False,False,False,False,False,False]]
              print(board)
          else:
            await interaction.response.send_message("its not your turn")

    #@discord.ui.Button(style=discord.ButtonStyle.primary, label="Give up", row=4,custom_id=)
    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="⬜", row=1,custom_id="persistent_view:button_ttt_2_callback")
    async def button_ttt_2_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      global mark
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[0] == interaction.user.id:
              ttt_list_2[4][1] = ":regional_indicator_x:"
              mark = ":regional_indicator_x:"
            else:
              ttt_list_2[4][1] = ":o2:"
              mark = ":o2:"
            gameOver = False
            view_ttt=None
            send = interaction.response.send_message
            if checkWinner(mark, ttt_list_2[4],gameOver) == True:
              interaction.respond(f"<@{interaction.author.id}> win and get the entire money.")
              await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
            else:
              if ttt_list_2[3] == ttt_list_2[0]:
                ttt_list_2[3] = ttt_list_2[1]
              else:
                ttt_list_2[3] = ttt_list_2[0]
              await interaction.message.edit(f"It was <@{interaction.user.id}> turn so now it's <@{ttt_list_2[3]}> turn.", view=button_update(view_ttt=view_ttt, ttt_list_2=ttt_list_2))

    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="⬜", row=1,custom_id="persistent_view:button_ttt_3_callback")
    async def button_ttt_3_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      global mark
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[0] == interaction.user.id:
              ttt_list_2[4][2] = ":regional_indicator_x:"
              mark = ":regional_indicator_x:"
            else:
              ttt_list_2[4][2] = ":o2:"
              mark = ":o2:"
            gameOver = False
            view_ttt=None
            send = interaction.response.send_message
            if checkWinner(mark, ttt_list_2[4],gameOver) == True:
              interaction.respond(f"<@{interaction.author.id}> win and get the entire money.")
              await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
            else:
              if ttt_list_2[3] == ttt_list_2[0]:
                ttt_list_2[3] = ttt_list_2[1]
              else:
                ttt_list_2[3] = ttt_list_2[0]
              await interaction.message.edit(f"It was <@{interaction.user.id}> turn so now it's <@{ttt_list_2[3]}> turn.", view=button_update(view_ttt=view_ttt, ttt_list_2=ttt_list_2))

    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="⬜", row=2,custom_id="persistent_view:button_ttt_4_callback")
    async def button_ttt_4_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      global mark
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[0] == interaction.user.id:
              ttt_list_2[4][3] = ":regional_indicator_x:"
              mark = ":regional_indicator_x:"
            else:
              ttt_list_2[4][3] = ":o2:"
              mark = ":o2:"
            gameOver = False
            view_ttt=None
            send = interaction.response.send_message
            if checkWinner(mark, ttt_list_2[4],gameOver) == True:
              interaction.respond(f"<@{interaction.author.id}> win and get the entire money.")
              await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
            else:
              if ttt_list_2[3] == ttt_list_2[0]:
                ttt_list_2[3] = ttt_list_2[1]
              else:
                ttt_list_2[3] = ttt_list_2[0]
              await interaction.message.edit(f"It was <@{interaction.user.id}> turn so now it's <@{ttt_list_2[3]}> turn.", view=button_update(view_ttt=view_ttt, ttt_list_2=ttt_list_2))

    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="⬜", row=2,custom_id="persistent_view:button_ttt_5_callback")
    async def button_ttt_5_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      global mark
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[0] == interaction.user.id:
              ttt_list_2[4][4] = ":regional_indicator_x:"
              mark = ":regional_indicator_x:"
            else:
              ttt_list_2[4][4] = ":o2:"
              mark = ":o2:"
            gameOver = False
            view_ttt=None
            send = interaction.response.send_message
            if checkWinner(mark, ttt_list_2[4],gameOver) == True:
              interaction.respond(f"<@{interaction.author.id}> win and get the entire money.")
              await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
            else:
              if ttt_list_2[3] == ttt_list_2[0]:
                ttt_list_2[3] = ttt_list_2[1]
              else:
                ttt_list_2[3] = ttt_list_2[0]
              await interaction.message.edit(f"It was <@{interaction.user.id}> turn so now it's <@{ttt_list_2[3]}> turn.", view=button_update(view_ttt=view_ttt, ttt_list_2=ttt_list_2))

    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="⬜", row=2,custom_id="persistent_view:button_ttt_6_callback")
    async def button_ttt_6_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      global mark
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[0] == interaction.user.id:
              ttt_list_2[4][5] = ":regional_indicator_x:"
              mark = ":regional_indicator_x:"
            else:
              ttt_list_2[4][5] = ":o2:"
              mark = ":o2:"
            gameOver = False
            view_ttt=None
            send = interaction.response.send_message
            if checkWinner(mark, ttt_list_2[4],gameOver) == True:
              interaction.respond(f"<@{interaction.author.id}> win and get the entire money.")
              await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
            else:
              if ttt_list_2[3] == ttt_list_2[0]:
                ttt_list_2[3] = ttt_list_2[1]
              else:
                ttt_list_2[3] = ttt_list_2[0]
              await interaction.message.edit(f"It was <@{interaction.user.id}> turn so now it's <@{ttt_list_2[3]}> turn.", view=button_update(view_ttt=view_ttt, ttt_list_2=ttt_list_2))

    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="⬜", row=3,custom_id="persistent_view:button_ttt_7_callback")
    async def button_ttt_7_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      global mark
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[0] == interaction.user.id:
              ttt_list_2[4][6] = ":regional_indicator_x:"
              mark = ":regional_indicator_x:"
            else:
              ttt_list_2[4][6] = ":o2:"
              mark = ":o2:"
            gameOver = False
            view_ttt=None
            send = interaction.response.send_message
            if checkWinner(mark, ttt_list_2[4],gameOver) == True:
              interaction.respond(f"<@{interaction.author.id}> win and get the entire money.")
              await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
            else:
              if ttt_list_2[3] == ttt_list_2[0]:
                ttt_list_2[3] = ttt_list_2[1]
              else:
                ttt_list_2[3] = ttt_list_2[0]
              await interaction.message.edit(f"It was <@{interaction.user.id}> turn so now it's <@{ttt_list_2[3]}> turn.", view=button_update(view_ttt=view_ttt, ttt_list_2=ttt_list_2))

    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="⬜", row=3,custom_id="persistent_view:button_ttt_8_callback")
    async def button_ttt_8_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      print("test-8")
      global mark
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[0] == interaction.user.id:
              ttt_list_2[4][7] = ":regional_indicator_x:"
              mark = ":regional_indicator_x:"
            else:
              ttt_list_2[4][7] = ":o2:"
              mark = ":o2:"
            gameOver = False
            view_ttt=None
            send = interaction.response.send_message
            if checkWinner(mark, ttt_list_2[4],gameOver) == True:
              interaction.respond(f"<@{interaction.author.id}> win and get the entire money.")
              await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
            else:
              if ttt_list_2[3] == ttt_list_2[0]:
                ttt_list_2[3] = ttt_list_2[1]
              else:
                ttt_list_2[3] = ttt_list_2[0]
              await interaction.message.edit(f"It was <@{interaction.user.id}> turn so now it's <@{ttt_list_2[3]}> turn.", view=button_update(view_ttt=view_ttt, ttt_list_2=ttt_list_2))

    @discord.ui.button(style=discord.ButtonStyle.secondary, emoji="⬜", row=3,custom_id="persistent_view:button_ttt_9_callback")
    async def button_ttt_9_callback(self, button: discord.ui.button,interaction:discord.Interaction):
      global mark
      for ttt_list_2 in board:
        if ttt_list_2[2] == interaction.message.id and ttt_list_2[0] == interaction.user.id or ttt_list_2[2] == interaction.message.id and ttt_list_2[1] == interaction.user.id:
          if ttt_list_2[3] == interaction.user.id:
            if ttt_list_2[0] == interaction.user.id:
              ttt_list_2[4][8] = ":regional_indicator_x:"
              mark = ":regional_indicator_x:"
            else:
              ttt_list_2[4][8] = ":o2:"
              mark = ":o2:"
            gameOver = False
            view_ttt=None
            send = interaction.response.send_message
            if checkWinner(mark, ttt_list_2[4],gameOver) == True:
              interaction.respond(f"<@{interaction.author.id}> win and get the entire money.")
              await update_bank(interaction.user, send, 2*ttt_list_2[5], mode = "wallet")
            else:
              if ttt_list_2[3] == ttt_list_2[0]:
                ttt_list_2[3] = ttt_list_2[1]
              else:
                ttt_list_2[3] = ttt_list_2[0]
              await interaction.message.edit(f"It was <@{interaction.user.id}> turn so now it's <@{ttt_list_2[3]}> turn.", view=button_update(view_ttt=view_ttt, ttt_list_2=ttt_list_2))

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


    @commands.slash_command()
    async def tictactoe_buttons(self, ctx, p2: Option(discord.Member, required=True), amount: Option(int, required=True)):
        global player1
        global player2
        global turn
        global gameOver
        global p1
        global p2_2
        global amount_2
        global new_games

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
          await ctx.respond(f"You cant use {amount}$. Use a number that is bigger than 0")
          return
        amount_2 = amount
        player1 = ""
        player2 = ""
        turn = ""
        gameOver = True

        p1 = ctx.author

        if p2 == ctx.author:
                await ctx.respond("Enter 2 different names. No game was started.")
                return
        p2_2 = p2
        


        button_p2_accept = Button(style=discord.ButtonStyle.green, label="accept")
        button_p2_declince = Button(style=discord.ButtonStyle.red, label="declince")
        view = View()
        view.add_item(button_p2_accept)
        view.add_item(button_p2_declince)
        start_message = await ctx.respond(f"<@{p2.id}>, click on the green button below this messages to accept this tic-tac-toe game and pay {amount}$ to enter or click on the red button to declince the game and pay nothing.", view=view)

        new_games.append([
          ctx.author.id,
          p2.id,
          amount,
          start_message.id
        ])

        async def button_p2_accept_callback(interaction):
          global new_games
          counter = 0
          for game_start in new_games:
            if game_start[3] == interaction.message.id:
              counter +=1
              if interaction.user != game_start[1]:
                await  ctx.send(f"<@{interaction.user.id}>, you are not allowed to use this button start a own tictactoe game")
                return
              if counter == len(new_games):
                return
          member = interaction.user      
          await new_member(member)
          user = member
          users_coins = await get_coins()
          coins_amt_str = users_coins[str(user.id)]
          coins_amt = int(coins_amt_str)

          if game_start[2] > coins_amt:
                await ctx.respond(f"You dont have that much money (You have {coins_amt}<:bot_icon:951868023503986699>)")
                return
          else:
                await interaction.response.edit_message(content="Game is started:", view=None)
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
                    global game_list
                    game_list = [["⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜","⬜"],[False,False,False,False,False,False,False,False,False]]
                    ttt_start_msg = await ctx.send(f"Ok <@{p1.id}> and <@{p2_2.id}>, a game was started. It's <@{p3.id}> turn.",view=PersistentView())
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
                await  interaction.respond(f"<@{interaction.user.id}>, you are not allowed to use this button, start a own tictactoe game")
                return
              else:
                await interaction.response.edit_message(content=f"<@{p1.id}>, {p2_2} dont want to play a game.", view=None)
                new_games.remove(game_start)



        #button_ttt_give_up.callback = button_ttt_give_up_callback
        button_p2_declince.callback = button_p2_declince_callback


        button_p2_accept.callback = button_p2_accept_callback


def setup(client):
    client.add_cog(tictactoe_buttons(client))