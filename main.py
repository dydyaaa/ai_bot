import asyncio, logging, os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from app.handlers import router

load_dotenv()
bot = Bot(token=os.getenv('TG_TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Завершение работы...')
        exit()