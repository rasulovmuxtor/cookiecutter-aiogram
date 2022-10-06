import os
from aiogram import Bot, Dispatcher, executor, types
import logging
from strings import get_language

TOKEN = os.getenv('BOT_API_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    lang = get_language(message.from_user.language_code)
    await bot.send_message(
        message.chat.id,
        lang.cmd_start.format(message.from_user.full_name)
    )


@dp.message_handler(commands=['faq'])
async def cmd_faq(message: types.Message):
    lang = get_language(message.from_user.language_code)
    await bot.send_message(
        message.chat.id,
        lang.faq
    )


@dp.message_handler(commands=['contact'])
async def cmd_contact(message: types.Message):
    lang = get_language(message.from_user.language_code)
    await bot.send_message(
        message.chat.id,
        lang.contact
    )


{% if cookiecutter.use_fastapi == 'y' %}
if __name__ == '__main__' and not os.getenv('HOST'):
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
{% else %}
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
{% endif %}
