import requests
import rlog
logger = rlog.rlogger

# Getting Weather
def get_weather(area_entry,display="all"):
    # Area code checking
    if area_entry == 1:
        logger.warn(f"{area_entry} : Not Found")
        return("ERROR")
    # Requests
    logger.debug(f"{area_entry} : Getting")
    forecast_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_entry}.json"
    overview_url = f"https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{area_entry}.json"
    forecast_json = requests.get(forecast_url).json()
    overview_json = requests.get(overview_url).json()
    # Weathers
    weather_time = forecast_json[0]["timeSeries"][0]["timeDefines"][0]
    weather = forecast_json[0]["timeSeries"][0]["areas"][0]["weathers"][0]
    # Overview
    overview_time = overview_json["reportDatetime"]
    overview = overview_json["text"]
    # Remove Zenkaku-Space
    weather = weather.replace('　', '')
    overview = overview.replace('　', '')
    # return controls
    if display == "all":
        # returning all texts
        return(f"{weather_time}\n{weather}\n\n{overview_time}\n{overview}")
    elif display == "weather":
        # returning only weather info
        return(f"{weather_time}\n{weather}")
    elif display == "overview":
        # returning only overview text
        return(f"{overview_time}\n{overview}")
    else:
        # missmatch -> All Texts
        return(f"{weather_time}\n{weather}\n\n{overview_time}\n{overview}")

# Debug
if __name__ == "__main__":
    from region import get_region
    get_pref = input("Pref > ")
    if get_region(get_pref) == 1:
        print("ERROR")
    else:
        print(get_weather(get_region(get_pref)))
