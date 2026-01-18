import config as cfg

try:
    FONT = cfg.font
except:
    FONT = "slant"


def chech_version() -> bool | str:
    version = f"{cfg.version}"
    try:
        import requests
        from bs4 import BeautifulSoup as bs

        URL = r"https://github.com/Sk1lizz/switch_siteV3/blob/main/files/config/config.json"

        r = requests.get(URL)

        soup = bs(r.text, "html.parser")

        versions_text = soup.find_all('div', class_='repository-content')
        version_split = (str(versions_text).split('version'))[1]
        version_clear = version_split[6::]
        version_split_2 = (version_clear.split('","'))[0]
        version_online = version_split_2[:-1]

        if (version == version_online):
            return True
        else:
            return version_online

    except Exception as e:
        return "Error"


def get_version() -> str | None:
    if bool(chech_version() == "Error"):
        text = (cfg.version_error).replace("<version>", f"{cfg.version}").replace("<packages>", "requests, bs4")
        return text
    elif bool(chech_version() == True):
        return None
    else:
        text = (cfg.version_false).replace("<old_version>", cfg.version).replace("<new_version>", f"{chech_version()}").replace("<git>", f"{cfg.git}")
        return text

def main_menu() -> None:
    try:
        from pyfiglet import figlet_format
        

        text_main = figlet_format(text=f"{cfg.name_console}", font=FONT)
    except:
        text_main = f"{cfg.name_console}"

    
    text_body = """<2> - <switch_menu>\n<3> - <wiki_menu>\n<8> - <help_menu>\n<9> - <info_menu>\n<0> - <exit>"""


def switch_menu()-> None:
    pass


def wiki_menu() -> None:
    pass


def help_menu() -> None:
    pass


def info_menu() -> None:
    pass