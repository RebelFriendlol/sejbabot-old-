from fileinput import close
from http import client
from multiprocessing.connection import wait
import string
from tracemalloc import stop
from typing import AnyStr
import discord
from discord.ext import commands
import random
from discord.ext import tasks 


TOKEN = ' '
description = '''Sejba je duzoooo'''

#prefix
bot = commands.Bot(command_prefix='?', description=description)

#variable for task
odp = ['Shiiiroooouu!!!','Głodna jestem (`ー´)','Hambarga (≧◡≦)']

        

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    mytask.start()

#after 1 minute bot is sending message from array
@tasks.loop(minutes=1)
async def mytask():
    await bot.wait_until_ready()
    channel = bot.get_channel(" ") #CHANNEL ID
    await channel.send(odp[random.randint(0,2)])

#turning bot off
@bot.command()
@commands.is_owner()
async def dobranoc(ctx):
    await ctx.send("Dobranoc :sleeping:")
    await ctx.bot.logout()


bot.run(TOKEN)