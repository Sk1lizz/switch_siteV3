import config as cfg

from console import main_menu, switch_menu, wiki_menu, help_menu, info_menu

try:
    from bot import main_bot
except:
    def main_bot() -> None: return None

try:
    from app import main_app
except:
    def main_app() -> None: return None

# __version__ = "v3.0.1 | 26.01.2026"

def console() -> None | bool:
    rq_text = cfg.request_message

    main_menu()

    while True:
        try:
            rq = input(rq_text)
        except KeyboardInterrupt:
            break
        except Exception as e:
            break


        match rq:
            case "1":
                main_menu()
                continue
            
            case "2":
                switch_menu()
                

            case "3":
                wiki_menu()

            case "8":
                help_menu()
            
            case "9":
                info_menu()
                
            case "0":
                print(f"\n{cfg.end_message}\n")
                break
        main_menu()



def bot() -> None | bool:
    main_bot()
    


def app() -> None | bool:
    main_app()


def main() -> None:
    if bool(cfg.enable_console):
        try:
            console()
        except:
            print("...")
    
    
    elif bool(cfg.enable_bot):
        if not (cfg.TOKEN is None):
            try:
                bot()
            except:
                print("...")
        

    elif bool(cfg.enable_app):
        try:
            app()
        except:
            print("...")

    else:
        try:
            console()
        except:
            print("...")
    
if __name__ == "__main__":
    main()