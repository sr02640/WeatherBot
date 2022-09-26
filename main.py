#!/bin/env python
# Libraries
from turtle import title
import discord
from discord.ext import commands
from region import get_region
from weather import get_weather
from log_messages import command_exec
import logging
import logging.handlers

# Logging Initialization
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='bot.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,
    backupCount=5,
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Discord Token
token = ""

# var
bot = commands.Bot(command_prefix='!')

# Running Check
@bot.event
async def on_ready():
    logger.info("Ready")

# Help Message
@bot.command()
async def weatherhelp(ctx):
    await ctx.send("HELP MESSAGE")

# Weather Command Embed
# ToDo: Add Error Message
@bot.command()
async def weatherbot(ctx, area):
    area_code = get_region(area)
    weather_information = get_weather(area_code)
    embed = discord.Embed(color=0x4169e1)
    embed.add_field(name=f"{area}の天気",value=weather_information)
    await ctx.send(embed=embed)

bot.run(token, log_handler=None)
