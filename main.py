#!/bin/env python
### Libraries
import init_log as ilog
import setting
import rlog
import sys
import discord
from discord.ext import commands
from region import get_region, suffix_addition
from weather import get_weather

### Config
logger = rlog.rlogger
log_setLevel = setting.get_loglevel("stream")
args = sys.argv

### Discord Token
if args[1] == "-D" or args[1] == "--dev":
    # DevMode
    logger.info("Loaded token by DevMode (local)")
    token = setting.get_token("dev")
else:
    # Default
    logger.info("Loaded token (local)")
    token = setting.get_token("default")

### var
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
embed = discord.Embed(color=0x4169e1)

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
    if area_code == 1:
        # Error
        embed = discord.Embed(color = 0xffff00) # Change Color -> Yellow
        embed.add_field(name = "エラー", value = f"{area}は見つかりませんでした！")
    else: 
        # Normal
        w_info = get_weather(area_code, "weather")
        ov_info = get_weather(area_code, "overview")
        suf_area = suffix_addition(area)
        w_embed = discord.Embed(title = f"{suf_area}の天気", description = "天気情報は以下の通りです", color = 0x4169e1)
        w_embed.add_field(name = "予報", value = w_info)
        w_embed.add_field(name = "概要", value = ov_info)
    await ctx.send(embed = w_embed)

# Run
# Console Output
bot.run(token, reconnect=True, log_level=log_setLevel, root_logger=True)
