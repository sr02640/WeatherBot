# Libraries
from asyncore import file_dispatcher
import discord
import logging
import logging.handlers
import setting

# Config
file_setLevel = setting.get_loglevel("file")


# Variants
rlogger = logging.getLogger('Discord')
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')

### Initialize
handler = logging.handlers.RotatingFileHandler(
    filename='bot.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
handler.setFormatter(formatter)
rlogger.addHandler(handler)

### File Handler Setup
discord.utils.setup_logging(handler=handler, level=file_setLevel, root=False)

### Messages 
# [Debug] command executed: ********
def command_exec(cmd):
    return(f"Command executed - !{cmd}")