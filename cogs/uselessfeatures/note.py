from datetime import datetime, timedelta
from random import choice
from discord import Embed
from discord.ext.commands import Cog
import discord, json
from discord.ext import commands
from discord.utils import get
import datetime

class note(Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(name="note")
	async def notethis(self, ctx, note): #DAS DING IST CURSED, ÄNDERT NIX BITTE
		user = ctx.author
		with open("json_files/notes.json", "r") as f:
			notes = json.load(f)

		if str(user.id) not in notes:
			if True:
				notes[str(user.id)] = {}
				notes[str(user.id)]["1"] = note
				notes[str(user.id)]["2"] = ""
				notes[str(user.id)]["3"] = ""
				notes[str(user.id)]["4"] = ""
				notes[str(user.id)]["5"] = ""
				with open("json_files/notes.json", "w") as f:
					json.dump(notes,f)

		elif str(user.id) in notes:
			if True:
				if notes[str(user.id)]["1"] == "":
					notes[str(user.id)]["1"] = note
				elif notes[str(user.id)]["2"] == "":
					notes[str(user.id)]["2"] = note
				elif notes[str(user.id)]["3"] == "":
					notes[str(user.id)]["3"] = note
				elif notes[str(user.id)]["4"] == "":
					notes[str(user.id)]["4"] = note
				elif notes[str(user.id)]["5"] == "":
					notes[str(user.id)]["5"] = note
				else:
					await ctx.send(f"You can't have more than 5 notes.\nUse `.notes list` to list your notes, and `.notes delete X` to delete a note (with X as your note-number).\n<@{user.id}>")
				with open("json_files/notes.json", "w") as f:
					json.dump(notes,f)



def setup(bot):
	bot.add_cog(note(bot))