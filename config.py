import json

# __version__ = "v3.0.1 | 26.01.2026"

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

wiki_link = r"https://sk1lizz.gitbook.io/switch-site-docs/"

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
wiki_message = data_tg["wiki-message"]
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
progress_wiki_message = data_tg["progress-wiki-message"]

git = "https://github.com/Sk1lizz/switch_site"


font = data_console["font"]
name_console = data_console["name"]


# Сообщение из консоли
data_message_console = data_lang["main-body"]

version_message = data_message_console["version"]
version_false = version_message["version-false"]
version_error = version_message["version-error"]


console_message = data_message_console
main_menu_message = console_message["main-menu"]
switch_menu_message = console_message["switch-menu"]
wiki_menu_message = console_message["wiki-menu"]
help_menu_message = console_message["help-menu"]
info_menu_message = console_message["info-menu"]
exit_message = console_message["exit"]
end_message = console_message["end"]
request_message = console_message["request"]
help_text = console_message["help-text"]


switch_menu_setting = data_message_console["switch-menu-message"]

switch_on_message = switch_menu_setting["switch-on"]
switch_off_message = switch_menu_setting["switch-off"]
switch_add_message = switch_menu_setting["site-add"]
switch_delete_message = switch_menu_setting["site-delete"]
switch_list_message = switch_menu_setting["site-list"]


switch_menu = data_message_console["switch-message"]

switch_on_console = switch_menu["switch-on"]
switch_off_console = switch_menu["switch-off"]
switch_add_console = switch_menu["switch-add"]
switch_delete_console = switch_menu["switch-delete"]
site_list_console = switch_menu["site-list"]
error_activate = switch_menu["error-activate"]
error_deactivate = switch_menu["error-deactivate"]
site_input = switch_menu["site-input"]
error_site = switch_menu["error-site"]

info_menu_console = data_message_console["info-menu-message"]
name_message_console = info_menu_console["name"]
version_message_console = info_menu_console["version"]
creator_message_console = info_menu_console["creator"]
language_message_console = info_menu_console["language"]

# Текст из приложения
program_lang = data_lang["program"]
btn_add_site = program_lang["add-site"]
btn_delete_site = program_lang["delete-site"]
btn_update_list = program_lang["update-list"]
btn_activate = program_lang["activate"]
btn_deactivate = program_lang["deactivate"]