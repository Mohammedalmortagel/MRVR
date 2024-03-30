import asyncio
import random
from AarohiX import app
from pyrogram.types import (InlineKeyboardButton,                            InlineKeyboardMarkup, Message)
from pyrogram import filters, Clienttxt = ["يا أجمل من نطق اسمي على لسانه ♡","شتبي","وش بغيت","وش رايك فاللي يناديني بوت ؟ 🦦","اسمى سهيله ياحب 🙄❤️","ثانيه واحده بتشقط وجى🙄","اؤمر {1} شتريد؟❤️🥺",        ]        @app.on_message(filters.command(["بوت","المرتجل"]))async def ktbat(client: Client, message: Message):      a = random.choice(txt)      await message.reply(f"https://t.me/{app.username}?startgroup=true")
