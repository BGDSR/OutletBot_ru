from aiogram import types, Dispatcher

async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот и я работаю! 🎉")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
