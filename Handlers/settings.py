from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.storage import load_user_data, save_user_data

router=Router()

@router.message(lambda m: m.text=='Settings')
async def open_settings(msg:Message):
    kb=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Starting Balance',callback_data='edit_sb')],
        [InlineKeyboardButton(text='Daily Profit %',callback_data='edit_dp')],
        [InlineKeyboardButton(text='Days',callback_data='edit_days')]
    ])
    await msg.answer('Select parameter to edit:',reply_markup=kb)

@router.callback_query()
async def callbacks(cb:CallbackQuery):
    if cb.data.startswith('edit_'):
        key=cb.data.replace('edit_','')
        await cb.message.answer(f'Enter new value for {key}:')
        await cb.answer()
