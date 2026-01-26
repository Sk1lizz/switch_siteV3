from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
import config as cfg

# __version__ = "v3.0.1 | 26.01.2026"

main_keyboard = InlineKeyboardBuilder()

main_keyboard.button(text=f"{cfg.button_help}", callback_data="main:help")
main_keyboard.button(text=f"{cfg.button_info}", callback_data="main:info")
main_keyboard.button(text=f"{cfg.button_program}", callback_data="main:program")

main_keyboard.adjust(2, 1)


help_keyboard = InlineKeyboardBuilder()

help_keyboard.button(text=f"{cfg.button_wiki}", callback_data="help:wiki")
help_keyboard.button(text=f"{cfg.button_info}", callback_data="help:info")
help_keyboard.button(text=f"{cfg.button_git}", callback_data="help:git")

help_keyboard.adjust(1, 2)


reply_keyboard = ReplyKeyboardBuilder()

reply_keyboard.button(text=f"{cfg.button_help}")
reply_keyboard.button(text=f"{cfg.button_info}")

reply_keyboard.adjust(1, 1)


info_keyboard = InlineKeyboardBuilder()

info_keyboard.button(text=f"{cfg.button_wiki}", callback_data="info:wiki")

info_keyboard.adjust(1, 1)


program_keyboard = InlineKeyboardBuilder()
program_keyboard.button(text=f"{cfg.button_activate}", callback_data="program:activate")
program_keyboard.button(text=f"{cfg.button_deactivate}", callback_data="program:deactivate")
program_keyboard.button(text=f"{cfg.button_site_add}", callback_data="program:site_add")
program_keyboard.button(text=f"{cfg.button_site_delete}", callback_data="program:site_delete")
program_keyboard.button(text=f"{cfg.button_site_list}", callback_data="program:site_list")

program_keyboard.adjust(2, 2, 1)


activate_keyboard = InlineKeyboardBuilder()

activate_keyboard.button(text=f"{cfg.button_activate}", callback_data="program:activate")

activate_keyboard.adjust(1)


deactivate_keyboard = InlineKeyboardBuilder()

deactivate_keyboard.button(text=f"{cfg.button_deactivate}", callback_data="program:deactivate")

deactivate_keyboard.adjust(1)