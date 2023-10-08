from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot import const
from bot.utils import translater
from db.crud import create_user, get_histiry

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
async def translate_hend(message: types.Message) -> None:
    await message.reply('Okay, then enter the text you want to translate')


@router.message(F.text == "History")
async def history_hend(message: types.Message) -> None:
    user = await get_histiry(message.from_user.id)
    builder = ReplyKeyboardBuilder()
    for i in user:
        builder.add(types.KeyboardButton(text=str(i)[2:9]))
    builder.adjust(1)
    await message.reply(
        'Your history',
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


@router.message(F.text)
async def save_hend(message: types.Message) -> None:
    translate_text = await translater(message.text)
    await create_user(message, translate_text)
    await message.reply(f'Your text: {translate_text}')
