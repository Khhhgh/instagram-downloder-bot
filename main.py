from aiogram import Bot, Dispatcher, executor, types
import logging
from downloader import InstagramVideoDownloader
import shutil
import os

# ضع التوكن مباشرة هنا
BOT_TOKEN = "7610698647:AAGc0vKL1iYTchSGJowB7FzlLWhwrPTg3V4"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")

@dp.message_handler()
async def mainpart(message: types.Message):
    await message.answer("Video yuklanmoqda...")
    try:
        if message.text.startswith("https://www.instagram.com/") or message.text.startswith("https://instagram.com/"):
            txt_file, video_file, folder = InstagramVideoDownloader(message.text)
            with open(video_file, 'rb') as video, open(txt_file, 'r', encoding='utf-8') as comment:
                await message.answer_video(video, caption=comment.read())
    except Exception as e:
        await message.answer(f"❌ Xatolik yuz berdi: {e}")
    finally:
        if 'folder' in locals() and os.path.exists(folder):
            shutil.rmtree(folder)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
