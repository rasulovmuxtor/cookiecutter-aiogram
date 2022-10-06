import os
from fastapi import FastAPI
from bot import TOKEN as BOT_API_TOKEN, bot, dp
from aiogram import types, Bot

app = FastAPI()
HOST = os.getenv('HOST')
WEBHOOK_PATH = f"/bot/{BOT_API_TOKEN.split(':')[0]}"
WEBHOOK_URL = f'{HOST}{WEBHOOK_PATH}'


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/webhook/')
async def set_webhook():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=WEBHOOK_URL, max_connections=60)
    return {"message": "Ok"}


@app.post(WEBHOOK_PATH)
async def process_webhook(update: dict):
    telegram_update = types.Update(**update)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)
