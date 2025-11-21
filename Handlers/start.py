from aiogram import Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

@router.message(commands=['start'])
async def start_cmd(msg:Message):
    kb=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Today Plan')],[KeyboardButton(text='Settings')]],resize_keyboard=True)
    await msg.answer('Welcome!',reply_markup=kb)
