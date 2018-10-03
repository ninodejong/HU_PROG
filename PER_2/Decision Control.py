def seizoen(month):
    season = ''
    if 9 <= month <= 11:
        season = 'Herfst'
    elif 3 <= month <= 5:
        season = 'Lente'
    elif 6 <= month <= 8:
        season = 'Zomer'
    else:
        season = 'Winter'
    return season
print(seizoen(10))