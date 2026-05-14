import asyncio
import aiohttp
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from googletrans import Translator

TOKEN = "8678981844:AAHjTGAA8eEC3zTuBxo7T0vazt6c_XAZ_j4"
API_KEY = "5796872f7a1038c6cbf7c65f"
CURRENCY_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/UZS"

tarjimon = Translator()
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Assalomu alaykum! Men valyuta kursini aytuvchi va matnlarni tarjima qiluvchi botman.")

@dp.message(Command("kurs"))
async def command_kurs_handler(message: Message) -> None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(CURRENCY_URL) as response:
                if response.status == 200:
                    data = await response.json()
                    dollar = data["conversion_rate"]
                    await message.answer(f"💵 1 AQSH dollari bugun: **{dollar}** so'm")
                else:
                    await message.answer("⚠️ Kursni olishda xatolik yuz berdi.")
    except Exception as e:
        await message.answer(f"Xatolik: {e}")

@dp.message()
async def translate_handler(message: Message) -> None:
    try:
        result = tarjimon.translate(message.text, src="uz", dest="en")
        await message.answer(f"🇬🇧 **Inglizcha tarjimasi:**\n{result.text}")
    except Exception:
        await message.answer("❌ Tarjima qilishda muammo yuz berdi. Iltimos, keyinroq urinib ko'ring.")

async def main() -> None:
    bot = Bot(token=TOKEN)
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot to'xtatildi")