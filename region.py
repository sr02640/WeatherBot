area_code = {'北海道':'016000',
            '青森':'020000',
            '岩手':'030000',
            '宮城':'040000',
            '秋田':'050000',
            '山形':'060000',
            '福島':'070000',
            '茨城':'080000',
            '栃木':'090000',
            '群馬':'100000',
            '埼玉':'110000',
            '千葉':'120000',
            '東京':'130000',
            '神奈川':'140000',
            '新潟':'150000',
            '富山':'160000',
            '石川':'170000',
            '福井':'180000',
            '山梨':'190000',
            '長野':'200000',
            '岐阜':'210000',
            '静岡':'220000',
            '愛知':'230000',
            '三重':'240000',
            '滋賀':'250000',
            '京都':'260000',
            '大阪':'270000',
            '兵庫':'280000',
            '奈良':'290000',
            '和歌山':'300000',
            '鳥取':'310000',
            '島根':'320000',
            '岡山':'330000',
            '広島':'340000',
            '山口':'350000',
            '徳島':'360000',
            '香川':'370000',
            '愛媛':'380000',
            '高知':'390000',
            '福岡':'400000',
            '佐賀':'410000',
            '長崎':'420000',
            '熊本':'430000',
            '大分':'440000',
            '宮崎':'450000',
            '鹿児島':'460100',
            '沖縄':'471000'
            }

# suffix detection
def suffix_detection(raw_area):
    # "fu" detection
    if raw_area.endswith("府"):
        return(raw_area.removesuffix("府"))
    # "to" detection
    # BUG:京都検出不可
    elif raw_area.endswith("都"):
        return(raw_area.removesuffix("都"))
    # "ken" detection
    elif raw_area.endswith("県"):
        return(raw_area.removesuffix("県"))
    # Not detected -> raw
    else:
        return(raw_area)

# Return region name
def get_region(r_area):
    # Remove suffix
    fix_area = suffix_detection(r_area)
    # Not Found -> Returning 1
    return(area_code.get(fix_area, 1))

# adding "ken" ;for output
def suffix_addition():
    pass

# Debugs
if __name__ == '__main__':
    get_pref = input("Prefecture > ")
    debug_pref = get_region(get_pref)
    print(debug_pref)
