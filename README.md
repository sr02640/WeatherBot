# WeatherBot
気象庁のサイトからJSONを取得してDiscordに出力するBot(開発中)

必須モジュール:
* `discord`
* `discord.ext`
* `toml`
* `requests`
* `logging`

`token.txt`にトークンを書き込んで、`-D`もしくは`--dev`オプションを付けて実行すると`bot.toml`にトークン設定していなくてもトークンが設定されます。(DevMode)

気象庁サイト: https://www.jma.go.jp/
