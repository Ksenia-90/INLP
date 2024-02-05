import os
import datetime
import requests
import logging
import python_weather
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
API_TOKEN = "6735779820:AAGXWJdULP_-vQGf7b5jL6hjYi6EinX64sg"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
W_TOKEN = '2eafb8c858d644f5b50161026240202'



@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
	await message.reply("Please type the city name!")

@dp.message_handler()
async def send_message(msg: types.Message):
    response = requests.get('http://api.weatherapi.com/v1/current.json?key=2eafb8c858d644f5b50161026240202&q=' + msg.text +'&aqi=no')
    data = response.json()
    t = data['current']['temp_c']
    await msg.reply("Dear " + msg.from_user.first_name + ", the weather in the city " + data['location']['name']
                    + " in the country " + data['location']['country'] + " is " + str(t) + " degrees!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)








