# Libs
import toml

# Load config file
with open('./bot.toml') as f:
    obj = toml.load(f)


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
