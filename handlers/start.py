import sqlite3

from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from keyboards.inline_buttons import (start_keyboard, admin_keyboard,)


async def start_button(message: types.Message):
    print(message)
    # try:
    Database().sql_insert_user_query(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    # except sqlite3.IntegrityError:
    #     pass
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Hello im your first bot",
        reply_markup=await start_keyboard()
    )

async def secret_word(message: types.Message):
    if message.from_user.id == 901306866:
        users = Database().sql_select_all_user_query()
        user_list = []
        for user in users:
            user_list.append(user['username'])

        await bot.send_message(
            chat_id=message.from_user.id,
            text="Long time no see, Admin!",
            reply_markup=await admin_keyboard()
        )
        # await bot.send_message(
        #     chat_id=message.from_user.id,
        #     text='\n'.join(user_list)
        # )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="You have no rights!"
        )

async def admin_user_list_call(call: types.CallbackQuery):
    users = Database().sql_select_all_user_query()
    user_list = []
    for user in users:
        if user['username']:
            user_list.append(user['username'])
        else:
            user_list.append(user['first_name'])
    await bot.send_message(
        chat_id=call.from_user.id,
        text='\n'.join(user_list)
    )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
    dp.register_message_handler(secret_word, lambda word: 'dorei' in word.text)
    dp.register_callback_query_handler(admin_user_list_call,
                                lambda word: word.data == "admin_user_list")

