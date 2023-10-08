from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.const import (
    STRAT_COMAND,
    KEY_TRANSLATE,
    KEY_HISTORY,
    FIRST_CONT_TEXT,
    START_MESSAGE,
    TRANSLATE_TEXT_REPLY,
    HISTORY_TEXT_REPLY,
    ON_TRANSLATE_TEXT_REPLY
)
from bot.utils import translater
from db.crud import create_user, get_histiry

router = Router()


@router.message(Command(STRAT_COMAND))
async def cmd_start(message: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text=KEY_TRANSLATE)],
        [types.KeyboardButton(text=KEY_HISTORY)]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(
        f'{START_MESSAGE}, {message.from_user.first_name}! '
        f'{FIRST_CONT_TEXT}',
        reply_markup=keyboard
    )


@router.message(F.text == KEY_TRANSLATE)
async def translate_hend(message: types.Message) -> None:
    await message.reply(TRANSLATE_TEXT_REPLY)


@router.message(F.text == KEY_HISTORY)
async def history_hend(message: types.Message) -> None:
    user = await get_histiry(message.from_user.id)
    builder = ReplyKeyboardBuilder()
    for i in user:
        builder.add(types.KeyboardButton(text=str(i)[2:9]))
    builder.adjust(1)
    await message.reply(
        HISTORY_TEXT_REPLY,
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


@router.message(F.text)
async def save_hend(message: types.Message) -> None:
    translate_text = await translater(message.text)
    await create_user(message, translate_text)
    await message.reply(f'{ON_TRANSLATE_TEXT_REPLY}: {translate_text}')
