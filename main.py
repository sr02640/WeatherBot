#!/bin/env python
### Libraries
from turtle import title
import discord
from discord.ext import commands
from region import get_region
from weather import get_weather
import setting
import log_messages
import logging
import logging.handlers

### Configuration Init
log_setLevel = setting.get_loglevel("client")
log_setLevel_logger = setting.get_loglevel("logger")

### Logging Initialization
logger = logging.getLogger('Discord')
# setLevel
if log_setLevel == "DEBUG":
    # DEBUG Level
    logger.setLevel(logging.DEBUG)
    # INFO Level
elif log_setLevel == "INFO":
    logger.setLevel(logging.INFO)
# setLevel for Logger
if log_setLevel_logger == "DEBUG":
    # DEBUG Level
    logging.getLogger('discord.http').setLevel(logging.DEBUG)
elif log_setLevel_logger == "INFO":
    # INFO Level
    logging.getLogger('discord.http').setLevel(logging.INFO)
# handler
handler = logging.handlers.RotatingFileHandler(
    filename='bot.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,
    backupCount=5,
)# formats
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

### Discord Token
token = setting.get_token()

### var
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Running Check
@bot.event
async def on_ready():
    logger.info("Ready")
    print("Ready (Check bot.log!")

# Help Message
# ToDo Embed
@bot.command()
async def weatherhelp(ctx):
    logger.info(log_messages.command_exec("weatherhelp"))
    await ctx.send("HELP MESSAGE")

# Weather Command Embed
# ToDo: Add Error Message
@bot.command()
async def weatherbot(ctx, area):
    logger.info(log_messages.command_exec(f"weatherbot {area}"))
    area_code = get_region(area)
    weather_information = get_weather(area_code)
    embed = discord.Embed(color=0x4169e1)
    embed.add_field(name=f"{area}の天気",value=weather_information)
    await ctx.send(embed=embed)

bot.run(token, log_handler=None)
