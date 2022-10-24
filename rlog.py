# Libraries
import discord
import logging
import logging.handlers
import setting

# Config
stream_setLevel = setting.get_loglevel("stream")
file_setLevel   = setting.get_loglevel("file")
http_setLevel   = setting.get_loglevel("http")
client_setLevel = setting.get_loglevel("client")
gtway_setLevel  = setting.get_loglevel("gateway")

# Variants
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')

### Initialize
# discord.http
if http_setLevel == "INFO":
    logging.getLogger('discord.http').setLevel(logging.INFO)
elif http_setLevel == "DEBUG":
    logging.getLogger('discord.http').setLevel(logging.DEBUG)
# discord.client
if client_setLevel == "INFO":
    logging.getLogger('discord.client').setLevel(logging.INFO)
elif client_setLevel == "DEBUG":
    logging.getLogger('discord.client').setLevel(logging.DEBUG)
# discord.gateway
if gtway_setLevel == "INFO":
    logging.getLogger('discord.gateway').setLevel(logging.INFO)
elif gtway_setLevel == "DEBUG":
    logging.getLogger('discord.gateway').setLevel(logging.DEBUG)
# file setup
handler = logging.handlers.RotatingFileHandler(filename='bot.log', encoding='utf-8', maxBytes=32 * 1024 * 1024)
handler.setFormatter(formatter)
# set logger
rlogger = logging.getLogger('Discord')
rlogger.addHandler(handler)

### File Handler Setup
# File Output
discord.utils.setup_logging(handler=handler, level=file_setLevel, root=False)

### Messages 
# [Debug] command executed: ********
def command_exec(cmd):
    return(f"Command executed - !{cmd}")