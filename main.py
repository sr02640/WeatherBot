#!/bin/env python
# Libraries
from turtle import title
import discord
from discord.ext import commands
from region import get_region
from weather import get_weather

# Discord Token
token = "OTgzMjQ3MzIyMTkwMzE1NTMy.GlIlRJ.eCFibkIiajO9SZBaDW-CxXwqjkTXYjdi4ooX_g"
# var
bot = commands.Bot(command_prefix='!')

# Running Check
@bot.event
async def on_ready():
    print('Ready')

# Help Message
@bot.command()
async def weatherhelp(ctx):
    await ctx.send("HELP MESSAGE")

# Weather Command
@bot.command()
async def weatherbot(ctx, area):
    area_code = get_region(area)
    weather_information = get_weather(area_code)
    await ctx.send(weather_information)

# Weather Command Embed
@bot.command()
async def wbem(ctx, area):
    area_code = get_region(area)
    weather_information = get_weather(area_code)
    embed = discord.Embed(color=0x4169e1)
    embed.add_field(name=f"{area}の天気",value=weather_information)
    await ctx.send(embed=embed)

bot.run(token)