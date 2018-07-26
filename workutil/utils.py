COLOR_DICT = dict(zip(
    "BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE".split(','),
    [i + 30 for i in range(8)]
))

STYLE_DICT = dict(zip(
    "NORMAL,BOLD".split(','),
    range(2)
))

def color_text(text, color="WHITE", style="NORMAL"):
    color_code = COLOR_DICT[color]
    style_code = STYLE_DICT[style]
    return '\033[{};{}m{}\033[1;m'.format(style_code, color_code, text)
