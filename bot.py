import asyncio
import logging
from config import TOKEN
import config as cfg 
import sys
import keyboards as kb
from switch import state_edit, switch_on, switch_off, switch_add, switch_delete, site_list

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()

site_waiting = False

sitelist = []
sitelist_callback = []

@dp.message(CommandStart())
async def start_command(message: Message) -> None:
    text_message = str(cfg.start_message).replace("<user>", f"{message.from_user.first_name}").replace("<bot_name>", f"{cfg.name_bot}")
    await message.answer(text=text_message, reply_markup=kb.main_keyboard.as_markup())


@dp.message(Command("help"))
async def help_command(message: Message) -> None:
    text_message = str(cfg.help_message)
    await message.answer(text=text_message, reply_markup=kb.help_keyboard.as_markup())


@dp.message(F.text == "Помощь")
async def help_text(message: Message) -> None:
    if site_waiting:
        pass
    else:
        text_message = str(cfg.help_message)
        await message.answer(text=text_message, reply_markup=kb.help_keyboard.as_markup())


@dp.message(F.text == "О проекте")
async def info_text(message: Message) -> None:
    if site_waiting:
        pass
    else:
        text_message = str(cfg.info_message).replace("<git>", f"{cfg.git}")
        await message.answer(text=text_message, reply_markup=kb.info_keyboard.as_markup())

@dp.message(F.text)
async def info_text(message: Message) -> None:
    global site_waiting
    if site_waiting:
        site_waiting = False

        site=str(message.text)

        switch_add(site=site)

        text_message = str((cfg.status_text_site_add).replace("<site>", f"{site}"))
        await message.answer(text=text_message, reply_markup=kb.program_keyboard.as_markup())
    else:
        text_message = str(cfg.help_message)
        await message.answer(text=text_message, reply_markup=kb.help_keyboard.as_markup())


@dp.callback_query(lambda c: c.data in ["main:help", "info:help"])
async def help_callback(callback: CallbackQuery) -> None:
    text_message = str(cfg.help_message)
    text_progress = str(cfg.progress_help_message)
    await callback.answer(text=text_progress)
    await callback.message.edit_text(text=text_message, reply_markup=kb.help_keyboard.as_markup())


@dp.callback_query(lambda c: c.data in ["main:info", "help:info"])
async def info_callback(callback: CallbackQuery) -> None:
    text_message = str(cfg.info_message).replace("<git>", f"{cfg.git}")
    text_progress = str(cfg.progress_info_message)
    await callback.answer(text=text_progress)
    await callback.message.edit_text(text=text_message, reply_markup=kb.info_keyboard.as_markup())


@dp.callback_query(lambda c: c.data in ["help:git"])
async def git_callback(callback: CallbackQuery) -> None:
    text_message = str(cfg.git_message).replace("<git>", f"{cfg.git}")
    text_progress = str(cfg.progress_git_message)
    await callback.answer(text=text_progress)
    await callback.message.edit_text(text=text_message, reply_markup=kb.main_keyboard.as_markup())


@dp.callback_query(lambda c: c.data in ["help:wiki"])
async def wiki_callback(callback: CallbackQuery) -> None:
    pass


@dp.callback_query(lambda c: c.data in ["main:program"])
async def program_callback(callback: CallbackQuery) -> None:
    text_message = str(cfg.program_message)
    text_progress = str(cfg.progress_program_message)
    await callback.answer(text=text_progress)
    await callback.message.edit_text(text=text_message, reply_markup=kb.program_keyboard.as_markup())


@dp.callback_query(lambda c: c.data in ["program:activate", "program:deactivate", "program:site_add", "program:site_delete", "program:site_list"])
async def program_edit_callback(callback: CallbackQuery) -> None:
    global current_state
    global sitelist
    global site_waiting
    global sitelist_callback

    if callback.data == "program:activate":
        if bool(state_edit(state=True)):

            state_edit(state=False)
        
            text_activate = str(cfg.progress_start_message)

            await callback.answer(text_activate)

            status_text = str(cfg.status_text_activate)
            await callback.message.edit_text(status_text, reply_markup=kb.deactivate_keyboard.as_markup())

            switch_on()
        
        else:
            text_error = str(cfg.progress_error_message)

            await callback.answer(text_error)

            status_text = str(cfg.status_text_error).replace("<status>", "включена.")
            await callback.message.edit_text(status_text, reply_markup=kb.program_keyboard.as_markup())

    elif callback.data == "program:deactivate":
        if bool(state_edit(state=False)):

            state_edit(state=True)
        
            text_deactivate = str(cfg.progress_stop_message)

            await callback.answer(text_deactivate)

            status_text = str(cfg.status_text_deactivate)
            await callback.message.edit_text(status_text, reply_markup=kb.activate_keyboard.as_markup())

            switch_off()
        
        else:
            text_error = str(cfg.progress_error_message)

            await callback.answer(text_error)

            status_text = str(cfg.status_text_error).replace("<status>", "выключена.")
            await callback.message.edit_text(status_text, reply_markup=kb.program_keyboard.as_markup())
    
    elif callback.data == "program:site_add":
        site_waiting = True

        text_waiting = str(cfg.progress_waiting_message)

        await callback.answer(text_waiting)

        status_text = str(cfg.waiting_site_text)
        await callback.message.edit_text(status_text)

        temp_sitelist = site_list().split("\n")
        sitelist = []
        for i in range(1, len(temp_sitelist)):
            sitelist.append(temp_sitelist[i])
    
    elif callback.data == "program:site_delete":
        D_keyboard = InlineKeyboardBuilder()

        temp_sitelist = site_list().split("\n")
        sitelist = []
        sitelist_callback = []

        for i in range(1, len(temp_sitelist)):
            sitelist.append(temp_sitelist[i])

        for i in sitelist:
            D_keyboard.button(text=f"{i}", callback_data=f"site:{i}")
            sitelist_callback.append(f"site:{i}")
        
        temp_sitelist = []

        D_keyboard.adjust(1)

        text_waiting = str(cfg.progress_delete_message)

        await callback.answer(text_waiting)

        status_text = str(cfg.waiting_site_delete_text)
        await callback.message.edit_text(status_text, reply_markup=D_keyboard.as_markup())

        D_keyboard = None
    
    elif callback.data == "program:site_list":
        D_keyboard = InlineKeyboardBuilder()

        temp_sitelist = site_list().split("\n")
        sitelist = []

        for i in range(1, len(temp_sitelist)):
            sitelist.append(temp_sitelist[i])

        for i in sitelist:
            D_keyboard.button(text=f"{i}", callback_data="main:program")

        temp_sitelist = []
        D_keyboard.adjust(1)

        text_waiting = str(cfg.progress_site_list)

        await callback.answer(text_waiting)

        status_text = str(cfg.status_text_site_list)
        await callback.message.edit_text(status_text, reply_markup=D_keyboard.as_markup())

        D_keyboard = None

@dp.callback_query(lambda c: c.data in sitelist_callback)
async def delete_callback(callback: CallbackQuery) -> None:
    site = str(callback.data).replace("site:", "")

    if switch_delete(site=site):
        text_delete = str(cfg.progress_delete_site)

        await callback.answer(text_delete)

        status_text = str(cfg.status_text_delete_true).replace("<site>", f"{site}")
        await callback.message.edit_text(status_text, reply_markup=kb.program_keyboard.as_markup())

    else:
        text_delete = str(cfg.progress_error_message)

        await callback.answer(text_delete)

        status_text = str(cfg.program_message)
        await callback.message.edit_text(status_text, reply_markup=kb.program_keyboard.as_markup())

async def main() -> None:
    await dp.start_polling(bot)


try:
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
except:
    print("INFO:Bot Stop.")
