import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.settings import router as settings_router
from handlers.plan import router as plan_router
from handlers.step_input import router as input_router

async def main():
    bot=Bot(BOT_TOKEN)
    dp=Dispatcher()
    dp.include_router(start_router)
    dp.include_router(settings_router)
    dp.include_router(plan_router)
    dp.include_router(input_router)
    await dp.start_polling(bot)

if __name__=='__main__': asyncio.run(main())
