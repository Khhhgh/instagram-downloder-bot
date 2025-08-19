from aiogram import Bot, Dispatcher, executor, types
import logging
from downloader import InstagramVideoDownloader
import shutil
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv("7610698647:AAGc0vKL1iYTchSGJowB7FzlLWhwrPTg3V4"))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}")

@dp.message_handler()
async def mainpart(message: types.Message):
    global downloaded
    await message.answer("Video yuklanmoqda...")
    if message.text.startswith("https://www.instagram.com/") or message.text.startswith("https://instagram.com/"):
        downloaded = InstagramVideoDownloader(message.text)
        with open(downloaded[1][0], 'rb') as video:
                with open(downloaded[0], "rb") as comment:
                    await message.answer_video(video, caption=comment.read().decode("utf-8"))
    shutil.rmtree(downloaded[2])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)
