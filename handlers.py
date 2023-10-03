from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder


import const
from utils import translater
from db.models import UserHistory

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message) -> None:
    kb = [
        [types.KeyboardButton(text="Translate")],
        [types.KeyboardButton(text="History")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(
        f'Hello, {message.from_user.first_name}! '
        f'{const.FIRST_CONT_TEXT}',
        reply_markup=keyboard
    )


@router.message(F.text == "Translate")
async def with_puree(message: types.Message):
    await message.reply('Okay, then enter the text you want to translate')


@router.message(F.text == "History")
async def with_puree(message: types.Message):
    user = await UserHistory.get_histori(message)
    builder = ReplyKeyboardBuilder()
    for i in user.message_inp:
        builder.add(types.KeyboardButton(text=str(i)[:9]))
    builder.adjust(1)
    await message.reply(
        'Your history',
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


@router.message(F.text)
async def with_puree(message: types.Message):
    text = await translater(str(message))
    await UserHistory.save(message, text)
    await message.reply(f'Your text: {text}')
