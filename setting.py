##### Load : Ult-High Priority
# Libs
import toml
import os
import sys

# Load Dev Mode Token
if os.path.exists("./token.txt"):
    with open("./token.txt", "r") as f:
        dev_token = f.read()

# Try load config file
try:
    with open('./bot.toml') as f:
        obj = toml.load(f)
except FileNotFoundError:
    # Failed -> Generate File -> Exit Program
    with open("./bot.toml", "w") as f:
        data = {
                "DISCORD_TOKEN": "INSERT_TOKEN", 
                "LOG_LEVEL": {
                        "STREAM": "INFO",
                        "FILE": "DEBUG",
                        "HTTP": "INFO",
                        "CLIENT": "INFO",
                        "GTWAY": "INFO"
                    }
               }
        toml.encoder.dump(data, f)
        # Message
        print("Edit configuration file. (Regenerated)")
        sys.exit(0)

# Get Token
def get_token(mode = "default"):
    if mode == "default":
        return (obj["DISCORD_TOKEN"])
    elif mode == "dev":
        if os.path.exists("./token.txt"):
            return (dev_token)
        else:
            # Errors
            return (obj["DISCORD_TOKEN"])

# Get Log Level
def get_loglevel(req = "stream"):
    # Console Output
    if req == "stream":
        return (obj["LOG_LEVEL"]["STREAM"])
    # File Handler
    elif req == "file":
        return (obj["LOG_LEVEL"]["FILE"])
    # discord.http
    elif req == "http":
        return (obj["LOG_LEVEL"]["HTTP"])
    # discord.client
    elif req == "client":
        return (obj["LOG_LEVEL"]["CLIENT"])
    # discord.gateway
    elif req == "gateway":
        return (obj["LOG_LEVEL"]["GTWAY"])
    # all
    elif req == "all":
        return (obj["LOG_LEVEL"])
    # same
    else:
        return (obj["LOG_LEVEL"])

# Debugs
if __name__ == '__main__':
    print(obj)
    print(get_token())
    print(get_loglevel("all"))
