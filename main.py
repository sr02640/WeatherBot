#!/bin/env python
### Libraries
import setting
import rlog
from turtle import title
import discord
from discord.ext import commands
from region import get_region
from weather import get_weather

### Config
log_setLevel = setting.get_loglevel("stream")

### Discord Token
token = setting.get_token()

### var
logger = rlog.rlogger
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Running Check
@bot.event
async def on_ready():
    logger.info("Ready")

# Help Message
# ToDo Embed
@bot.command()
async def weatherhelp(ctx):
    logger.info(rlog.command_exec("weatherhelp"))
    await ctx.send("HELP MESSAGE")

# Weather Command Embed
# ToDo: Add Error Message
@bot.command()
async def weatherbot(ctx, area):
    logger.info(rlog.command_exec(f"weatherbot {area}"))
    area_code = get_region(area)
    weather_information = get_weather(area_code)
    embed = discord.Embed(color=0x4169e1)
    embed.add_field(name=f"{area}の天気",value=weather_information)
    await ctx.send(embed=embed)

# Run
# Console Output
bot.run(token, reconnect=True, log_level=log_setLevel, root_logger=True)
