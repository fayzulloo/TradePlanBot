from aiogram import Router
from aiogram.types import Message
from database.storage import load_user_data

router=Router()

@router.message(lambda m: m.text=='Today Plan')
async def plan(msg:Message):
    d=load_user_data(msg.from_user.id)
    if not d:
        await msg.answer('No plan data set.')
        return
    await msg.answer(f"Plan:\nStart: {d.get('sb')}\nProfit: {d.get('dp')}%\nDays: {d.get('days')}")
