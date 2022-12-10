def calc_pm10(pm10: int):
    if pm10<=54:
        BP_Hi = 54
        BP_Lo = 0
        I_Hi = 50
        I_Lo = 0
    elif pm10<=154:
        BP_Hi = 154
        BP_Lo = 55
        I_Hi = 100
        I_Lo = 51
    elif pm10<=254:
        BP_Hi = 254
        BP_Lo = 155
        I_Hi = 150
        I_Lo = 101
    else:
        BP_Hi = 354
        BP_Lo = 255
        I_Hi = 200
        I_Lo = 151
    return (I_Hi-I_Lo)/(BP_Hi-BP_Lo)*(pm10 - BP_Lo) +I_Lo

def calc_CO(co: float):
    if co<=4.4:
        BP_Hi = 4.4
        BP_Lo = 0
        I_Hi = 50
        I_Lo = 0
    elif co<=9.4:
        BP_Hi = 9.4
        BP_Lo = 4.5
        I_Hi = 100
        I_Lo = 51
    elif co<=12.4:
        BP_Hi = 12.4
        BP_Lo = 9.5
        I_Hi = 150
        I_Lo = 101
    else:
        BP_Hi = 15.4
        BP_Lo = 12.5
        I_Hi = 200
        I_Lo = 151
    return (I_Hi-I_Lo)/(BP_Hi-BP_Lo)*(co - BP_Lo) +I_Lo