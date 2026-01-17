import config as cfg

try:
    FONT = cfg.font
except:
    FONT = "slant"

def hi() -> None:
    try:
        from pyfiglet import figlet_format

        text_main = figlet_format(text=f"{cfg.name_console}", font=FONT)
    except:
        text_main = f"{cfg.name_console}"

    
    text_body = ""

hi()