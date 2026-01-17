import json

with open(r"files\config\bot.json", "r", encoding='utf-8') as file:
    data_bot = json.load(file)

with open(r"files\config\config.json", "r", encoding='utf-8') as file:
    data_config = json.load(file)

with open(r"files\config\console.json", "r", encoding='utf-8') as file:
    data_console = json.load(file)

lang = data_config["language"]

try:
    path_to_lang = rf"files\config\language\{lang}.json"
except:
    path_to_lang = r"files\config\language\Ru-ru.json"

try:
    with open(path_to_lang, "r", encoding='utf-8') as file:
        data_lang = json.load(file)
except:
    pass

TOKEN = data_bot["token"]
name_bot = data_bot["name"]

IP_BLOCK = data_config["ip-block"]
enable_bot = data_config["bot-telegram"]
enable_app = data_config["app"]
enable_console = data_config["console"]

config_path_to_hosts = data_config["path"]

name = data_config["name"]
version = data_config["version"]
creator = data_config["creator"]

# Сообщения из бота
data_tg = data_lang["telegram-bot"]
button = data_tg["button"]

button_help = button["help"]
button_info = button["info"]
button_program = button["program"]
button_wiki = button["wiki"]
button_git = button["git"]
button_activate = button["activate"]
button_deactivate = button["deactivate"]
button_site_add = button["site-add"]
button_site_delete = button["site-delete"]
button_site_list = button["site-list"]

start_message = data_tg["start-message"]
help_message = data_tg["help-message"]
info_message = data_tg["info-message"]
git_message = data_tg["git-message"]
program_message = data_tg["program-message"]
status_text_activate = data_tg["status-text-activate"]
status_text_deactivate = data_tg["status-text-deactivate"]
status_text_error = data_tg["status-text-error"]
waiting_site_text = data_tg["waiting-site-text"]
waiting_site_delete_text = data_tg["waiting-site-delete-text"]
status_text_delete_true = data_tg["status-text-delete-true"]
status_text_site_list = data_tg["status-text-site-list"]
status_text_site_add = data_tg["status-text-site-add"]

progress_help_message = data_tg["progress-help-message"]
progress_info_message = data_tg["progress-info-message"]
progress_git_message = data_tg["progress-git-message"]
progress_program_message = data_tg["progress-program-message"]
progress_start_message = data_tg["progress-start-message"]
progress_stop_message = data_tg["progress-stop-message"]
progress_error_message = data_tg["progress-error-message"]
progress_waiting_message = data_tg["progress-waiting-message"]
progress_delete_message = data_tg["progress-delete-message"]
progress_delete_site = data_tg["progress-delete-site"]
progress_site_list = data_tg["progress-site-list"]

git = "https://github.com/Sk1lizz/switch_site"

font = data_console["font"]
name_console = data_console["name"]