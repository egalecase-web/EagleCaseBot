import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import WebAppInfo

TOKEN = "8782810618:AAGBA17vhjNc42Cu8Hfu6QOuPPW3Iy1bAcU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    
    builder.row(types.InlineKeyboardButton(
        text="🎮 Играть", 
        web_app=WebAppInfo(url="https://google.com"))
    )
    
    builder.row(
        types.InlineKeyboardButton(text="💬 Чат", url="https://t.me/EagleChatCase"),
        types.InlineKeyboardButton(text="📢 Канал", url="https://t.me/EagleCase")
    )

    text = (
        "🎁 Выигрывайте NFT-подарки своей мечты!\n\n"
        "Вам доступен ежедневный бесплатный кейс, а также кейсы, апгрейд, и контракты."
    )

    await message.answer(text, reply_markup=builder.as_markup())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
