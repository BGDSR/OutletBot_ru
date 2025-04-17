from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from handlers import main_handlers

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

main_handlers.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)