import discord
from discord.ext import commands
import random
from discord.ui import Button, View
import json
from bank_functions import new_member, get_coins, update_bank
from discord import Option

class tictactoe(commands.Cog):

    def __init__(self, client):
        self.client = client
    

    global board
    global winningConditions
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
    
    @commands.slash_command()
    async def tictactoe(self, ctx, p2: Option(discord.Member, required=True), amount: Option(int, required=True)):
        global count
        global player1
        global player2
        global turn
        global gameOver
        global p1
        global p2_2
        global amount_2

        member = ctx.author      
        await new_member(member)
        user = member
        users_coins = await get_coins()
        coins_amt_str = users_coins[str(user.id)]
        coins_amt = int(coins_amt_str)

        if amount > coins_amt:
            await ctx.respond(f"You dont have that much money (You have {coins_amt}<:bot_icon:951868023503986699>)")
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
        await ctx.respond(f"<@{p2.id}>, click on the green button below this messages to accept this tic-tac-toe game and pay $ to enter or click on the red button to declince the game and pay nothing.", view=view, delete_after=120)

        async def button_p2_accept_callback(interaction):
          global player1
          global player2
          global p1
          global p2_2
          if interaction.user != player2:
            ctx.send(f"<@{interaction.user.id}>, you are not allowed to use this button start a own tictactoe game")
            return
          member = interaction.user      
          await new_member(member)
          user = member
          users_coins = await get_coins()
          coins_amt_str = users_coins[str(user.id)]
          coins_amt = int(coins_amt_str)

          if amount > coins_amt:
            await ctx.respond(f"You dont have that much money (You have {coins_amt}<:bot_icon:951868023503986699>)")
            return
          else:
            await interaction.response.edit_message(content="Game is started:", view=None)
            global gameOver
            send = ctx.respond
            await update_bank(p1, send, -1*amount, mode = "wallet")
            await update_bank(p2_2, send, -1*amount, mode = "wallet")

            if bool(gameOver):
                global count
                global turn
                global board
                board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                        ":white_large_square:", ":white_large_square:", ":white_large_square:",
                        ":white_large_square:", ":white_large_square:", ":white_large_square:"]
                turn = ""
                gameOver = False
                count = 0
                player1 = p1
                player2 = p2_2
        
                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]
        
                # determine who goes first
                num = random.randint(1, 2)
                if num == 1:
                    turn = player1
                    await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
                elif num == 2:
                    turn = player2
                    await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
            else:
                await ctx.respond("A game is already in progress! Finish it before starting a new one.")

        async def button_p2_declince_callback(interaction):
            global p2_2
            if interaction.user != p2_2:
              ctx.send(f"<@{interaction.user.id}>, you are not allowed to use this button start a own tictactoe game")
              return
            await interaction.response.edit_message(content=f"<@{p1.id}>, {p2_2} dont want to play a game.", view=None)

        button_p2_accept.callback = button_p2_accept_callback
        button_p2_declince.callback = button_p2_declince_callback


        


    @commands.slash_command()
    async def tttend(self, ctx):
      global player1
      global player2
      global gameOver
      global p2_2
      global p1
      global amount_2
      if ctx.author == player1 or player2:
        gameOver = True
        send = ctx.respond
        if ctx.author == p1:
          await update_bank(p2_2, send, 2*amount_2, mode = "wallet")
          await ctx.respond(f"you gave up, <@{p2_2.id}> won and got the money")
        elif ctx.author == p2_2:
          await update_bank(p1, send, 2*amount_2, mode = "wallet")
          await ctx.respond(f"you gave up, <@{p1.id}> won and got the money")
                    
    
    @commands.slash_command(name="place", description="For Tic-Tac-Toe game")
    async def place(self, ctx, pos1: int):
        global turn
        global player1
        global player2
        global board
        global count
        global gameOver
        global amount_2
        global p1
        global p2_2

        pos = pos1
        if not gameOver:
            mark = ""                
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                    board[pos - 1] = mark
                    count += 1
    
                    # print the board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            if x == 2:
                                await ctx.respond(line)
                            else:
                                await ctx.send(line)
                            line = ""
                        else:
                            line += " " + board[x]
    
                    for condition in winningConditions:
                        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                            gameOver = True
                    send = ctx.respond
                    if gameOver == True:
                        if mark == ":regional_indicator_x:":
                            await update_bank(p1, send, 2*amount_2, mode = "wallet")
                            await ctx.send(f"<@{p1.id}> wins and got the entire money!")
                        elif mark == ":o2:":
                            await update_bank(p2_2, send, 2*amount_2, mode = "wallet")
                            await ctx.send(f"<@{p2_2.id}> wins and got the entire money!")
    
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("It's a tie! Both got their money back.")
                        await update_bank(p1, send, amount_2, mode = "wallet")
                        await update_bank(p2_2, send, amount_2, mode = "wallet")

    
                    # switch turns
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                else:
                    await ctx.respond("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
            else:
                await ctx.respond("It is not your turn.")
        else:
            await ctx.respond("Please start a new game using the /tictactoe command.")
    
    
    def checkWinner(self, winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True
          

def setup(client):
    client.add_cog(tictactoe(client))