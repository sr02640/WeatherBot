#!/bin/env python
# Libraries
from turtle import title
import discord
from discord.ext import commands
from region import get_region
from weather import get_weather
from log_messages import command_exec
import logging

# Logging Initialization
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
lf = logging.FileHandler(filename="bot.log")
lf.setLevel(logging.DEBUG)
log_format = logging.Formatter('[%(levelname)s][%(asctime)s] - %(message)s')
lf.setFormatter(log_format)
logger.addHandler(lf)

# Discord Token
token = ""
logger.info("Token setting")

# var
bot = commands.Bot(command_prefix='!')

# Running Check
@bot.event
async def on_ready():
    logger.info("Ready")

# Help Message
@bot.command()
async def weatherhelp(ctx):
    logger.debug(command_exec("weatherhelp"))
    await ctx.send("HELP MESSAGE")

# Weather Command Embed
@bot.command()
async def weatherbot(ctx, area):
    logger.debug(command_exec(f"weatherbot {area}"))
    area_code = get_region(area)
    weather_information = get_weather(area_code)
    embed = discord.Embed(color=0x4169e1)
    embed.add_field(name=f"{area}の天気",value=weather_information)
    await ctx.send(embed=embed)

bot.run(token)
