import config as cfg

from switch import switch_add, switch_delete, switch_off, switch_on, site_list, filter_site

try:

    from pyfiglet import figlet_format
    FONT = cfg.font
    __test_text = figlet_format(text="TEST", font=FONT)
except:
    FONT = "slant"

# __version__ = "v3.0.1 | 26.01.2026"

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
        text = (cfg.version_error).replace("<version>", f"{cfg.version}")\
            .replace("<packages>", "requests, bs4")
        return text
    elif bool(chech_version() == True):
        return None
    else:
        text = (cfg.version_false).replace("<old_version>", cfg.version)\
            .replace("<new_version>", f"{chech_version()}")\
                .replace("<git>", f"{cfg.git}")
        return text

def main_menu() -> None:
    try:
        from pyfiglet import figlet_format
        
        text_main = figlet_format(text=f"{cfg.name_console}", font=FONT)
    except:
        text_main = f"\n{cfg.name_console}\n"

    text_body = ("""<2> - <switch_menu>\n<3> - <wiki_menu>\n<8> - <help_menu>\n<9> - <info_menu>\n<0> - <exit>""")\
        .replace("<switch_menu>", cfg.switch_menu_message).replace("<wiki_menu>", cfg.wiki_menu_message)\
            .replace("<help_menu>", cfg.help_menu_message).replace("<info_menu>", cfg.info_menu_message)\
                .replace("<exit>", cfg.exit_message)

    text = f"{text_main}\n{text_body}"

    print(text)



def switch_menu()-> None:
    try:
        from pyfiglet import figlet_format
        
        text_main = figlet_format(text=f"{cfg.name_console}", font=FONT)
    except:
        text_main = f"\n{cfg.name_console}\n"

    text_body = ("""<1> - <switch_on>\n<2> - <switch_off>\n<3> - <site_add>\n<4> - <site_delete>\n<5> - <site_list>\n<0> - <exit>""")\
        .replace("<switch_on>", cfg.switch_on_message).replace("<switch_off>", cfg.switch_off_message)\
            .replace("<site_add>", cfg.switch_add_message).replace("<site_delete>", cfg.switch_delete_message)\
                .replace("<site_list>", cfg.switch_list_message).replace("<exit>", cfg.exit_message)

    TEXT = f"{text_main}\n{text_body}"

    print(TEXT)

    while True:
        rq = input(cfg.request_message)

        match rq:
            case "0":
                print(cfg.exit_message)
                break

            case "1":
                if switch_on():
                    print(cfg.switch_on_console)
                else:
                    print(cfg.error_activate)

            case "2":
                if switch_off():
                    print(cfg.switch_off_console)
                else:
                    print(cfg.error_deactivate)

            case "3":
                site = input(cfg.site_input)
                if switch_add(site):
                    text = str(cfg.switch_add_console).replace("<site>", f"{filter_site(site)}")
                    print(text)
                else:
                    print(cfg.error_site)

            case "4":
                site = input(cfg.site_input)
                if switch_delete(site):
                    text = str(cfg.switch_delete_console).replace("<site>", f"{filter_site(site)}")
                    print(text)
                else:
                    print(cfg.error_site)

            case "5":
                text = f"{cfg.site_list_console}\n{site_list()}"
                print(text)
                
        
        print("\n\n", TEXT)


def wiki_menu() -> None:
    wiki = cfg.wiki_link

    print(wiki)


def help_menu() -> None:
    link = cfg.wiki_link
    text = str(cfg.help_text).replace("<link>", link)
    print(text)

def info_menu() -> None:
    try:
        from pyfiglet import figlet_format
        
        text_main = figlet_format(text=f"{cfg.name_console}", font=FONT)
    except:
        text_main = f"\n        {cfg.name_console}\n"

    text_body = """\n---------Info---------\n\n<name> - <name_program>\n<version> - <version_program>\n<creator> - <creator_program>\n<language> - <language_program>\n\n--------Info----------"""\
        .replace("<name_program>", cfg.name_console).replace("<version_program>", cfg.version)\
            .replace("<creator_program>", cfg.creator).replace("<language_program>", cfg.lang)\
                .replace("<name>", cfg.name_message_console).replace("<version>", cfg.version_message_console)\
                    .replace("<creator>", cfg.creator_message_console).replace("<language>", cfg.language_message_console)

    print(text_main, text_body)

# main_menu()