# https://huzunluartemis.github.io/NobetciEczaneRobot/

from re import findall
from helper_funcs.eczaneFuncs import removespace

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

def getPhoneNumber(num:str, withnewline=False):
    num = removespace(num, withnewline=False)
    try:
        num = int(num)
        isdigit = True
    except:
        isdigit = False
    num = str(num)
    if num.startswith('+90') or isdigit:
        toret = f"Tıkla Ara: {num}"
    else:
        bitisik = "".join(findall(r'\d+', num))
        toret = f"Telefon: {num} | Tıkla Ara: {bitisik}"
    return f"\n{toret}" if withnewline else toret
