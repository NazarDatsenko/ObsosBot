import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ChatType
from aiogram.types import FSInputFile
from aiogram.filters import Command

bot = Bot(token=os.environ["BOT_TOKEN"])
dp = Dispatcher()

# Голосове по команді /hello
@dp.message(Command("hello"), lambda m: m.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP))
async def send_voice(message: types.Message):
    voice = FSInputFile("hello.ogg")
    await message.answer_voice(voice)

# Ключове слово "морозіла"
@dp.message(lambda m: m.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP))
async def keyword(message: types.Message):
    if "морозіла" in message.text.lower():
        await message.reply("Чую починається обсос мол.")

async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
