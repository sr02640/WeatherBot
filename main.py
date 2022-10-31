#!/bin/env python
### Libraries
from turtle import title
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

# Running Check
@bot.event
async def on_ready():
    logger.info("Ready")

# Help Message
# ToDo Embed
@bot.command()
async def weatherhelp(ctx):
    logger.info(rlog.command_exec("weatherhelp"))
    desc = """
    !weatherhelp : ヘルプコマンド
    !weatherbot [地域(県)] : 天気情報を取得するコマンド
    
    天気情報は気象庁サイト(https://www.jma.go.jp/)から取得しています。
    """
    embed = discord.Embed(title = "コマンド一覧", description = desc, color=0x4169e1)
    await ctx.send(embed = embed)

# Weather Command Embed
# ToDo: Add Error Message
@bot.command()
async def weatherbot(ctx, area):
    logger.info(rlog.command_exec(f"weatherbot {area}"))
    area_code = get_region(area)
    if area_code == 1:
        # Error
        embed = discord.Embed(title = "エラー", description = f"{area}は見つかりませんでした！", color = 0xffff00)
    else: 
        # Normal
        w_info = get_weather(area_code, "weather")
        ov_info = get_weather(area_code, "overview")
        suf_area = suffix_addition(area)
        embed = discord.Embed(title = f"{suf_area}の天気", description = "天気情報は以下の通りです", color = 0x4169e1)
        embed.add_field(name = "予報", value = w_info)
        embed.add_field(name = "概要", value = ov_info)
    await ctx.send(embed = embed)

# Run
# Console Output
bot.run(token, reconnect=True, log_level=log_setLevel, root_logger=True)
