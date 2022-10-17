# Libs
import toml
import sys

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
                        "CLIENT": "INFO", 
                        "LOGGER": "INFO"
                    }
               }
        toml.encoder.dump(data, f)
        # Message
        print("Edit configuration file. (Regenerated)")
        sys.exit(0)

# Get Token
def get_token():
    return (obj["DISCORD_TOKEN"])

# Get Log Level
def get_loglevel(req = "client"):
    # Client
    if req == "client":
        return (obj["LOG_LEVEL"]["CLIENT"])
    # discord.http
    elif req == "logger":
        return (obj["LOG_LEVEL"]["LOGGER"])
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
