import asyncio
import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

# your bot's token, you can find one at @BotFather
TOKEN = ""

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data['bitcoin']['usd']


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    photo_file = FSInputFile("btc.jpg")

    await message.answer_photo(
        photo=photo_file,
        caption="Hi! I'm MerryBot. Type /btc to get current bitcoin's price."
    )


@dp.message(Command("btc"))
async def cmd_btc(message: types.Message):
    price = get_btc_price()
    await message.answer(f"Current Bitcoin price: ${price}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())