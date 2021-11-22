import discord
from discord.ext import commands
import colorama
from colorama import Fore
import asyncio
from webserver import keep_alive

import os

prefix = "$$"

keep_alive()
token = os.getenv("TOKEN")

bot = commands.Bot(command_prefix=prefix,
                   help_command=None,
                   case_insensitive=True,
                   self_bot=True)

@bot.command(pass_context=True)
async def auto(ctx):
	await ctx.message.delete()
	global dmcs
	dmcs = True
	while dmcs:
		async with ctx.typing():
			print("")

@bot.command()
async def stop(ctx):
	await ctx.message.delete()
	global dmcs
	dmcs = False

@bot.event
async def on_ready():
  print('online')

bot.run(token, bot=False)

