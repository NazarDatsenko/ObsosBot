import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ChatType
from aiogram.types import FSInputFile
from aiogram.filters import Command
import os

bot = Bot(token=os.environ["BOT_TOKEN"])
dp = Dispatcher()



@dp.message()
async def group_only(message: types.Message):
    if message.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
        return

@dp.message(Command("hello"), lambda m: m.chat.type in ("group", "supergroup"))
async def send_voice(message: types.Message):
    voice = FSInputFile("hello.ogg")
    await message.answer_voice(voice)

@dp.message()
async def keyword(message: types.Message):
    if message.chat.type.name.endswith("GROUP"):
        if "морозіла" in message.text.lower():
            await message.reply("Чую починається обсос мол.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
