import asyncio
import random
from pyrogram.types import InlineKeyboardButton
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from random import choice
from AarohiX import app
from config import BANNED_USERS, MUSIC_BOT_NAME
from AarohiX.misc import SUDOERS
import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

namd = [
f"اسمي {MUSIC_BOT_NAME} يقلبي 🙈",
f"عايز اي من {MUSIC_BOT_NAME} 😒",
f"اؤمرني يعيوني 🌚",
f"كل شويه {MUSIC_BOT_NAME} 😭",
f"قلبي ودقاته بينادي علي {MUSIC_BOT_NAME} 🔥🙈",
f"اسمي {MUSIC_BOT_NAME} يصحبي",
f"يسطا قولتلك اسمي {MUSIC_BOT_NAME} الاه",
f"نعم يحب",
f"قول يقلبو",
f"يسطا هوا عشان بحبك تصعدني؟",
f"يعم والله بحبك بس ناديلي ب {MUSIC_BOT_NAME}",
f"تعرف بالله هحبك أكتر لو ناديتلي {MUSIC_BOT_NAME}",
f"اي ي معلم مين مزعلك",
f"متصلي على النبي كدا",
f"مش فاضيلك نصايح وكلمني",
f"يسطا قولي مين مزعلك وعايزك تقعد وتتفرج على أخوك",
f"انجز عايزني أشقطلك مين؟",
f"شكلها منكدا عليك وجاي تطلعهم علينا",
f"ورحمة أبويا اسمي {MUSIC_BOT_NAME}",
]

@app.on_message(filters.command(["بوت", "البوت"], ""), group=39)
async def mreslam(client: Client, message: Message):
    barr = random.choice(namd) 
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])

    await message.reply_text(
       text=f"[{barr}](https://t.me/{bot_username}?startgroup=True)",
       disable_web_page_preview=True,
        reply_markup=keyboard
    )