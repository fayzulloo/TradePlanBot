from aiogram import Router
from aiogram.types import Message
from database.storage import load_user_data, save_user_data

router=Router()

@router.message()
async def catch_input(msg:Message):
    txt=msg.text.strip()
    # simplistic: detect if numeric
    if txt.isdigit():
        d=load_user_data(msg.from_user.id)
        # assume last edited key
        # placeholder simple logic
        d['sb']=int(txt)
        save_user_data(msg.from_user.id,d)
        await msg.answer('Updated.')
