import asyncio
from aiogram import Bot, Dispatcher, types
import os

bot = Bot(token=os.environ["BOT_TOKEN"])
dp = Dispatcher()


@dp.message()
async def hello(message: types.Message):
    await message.answer("Хай! Я бот для обсоса Морозіли мол.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
