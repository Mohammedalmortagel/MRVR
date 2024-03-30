import asyncio
import random
from AarohiX import app
from pyrogram.types import (InlineKeyboardButton,                            InlineKeyboardMarkup, Message)
from pyrogram import filters, Client
txt = ["يا أجمل من نطق اسمي على لسانه ♡","شتبي","وش بغيت","وش رايك فاللي يناديني بوت ؟ 🦦","اسمي\n{1}\nيحب","ثانيه واحده بتشقط وجى🙄",        ]   
@app.on_message(filters.command(["بوت","المرتجل"]))
async def ktbat(client: Client, message: Message):  
url= (f"https://t.me/{app.username}?startgroup=true")
a = random.choice(txt,url)      await message.reply(f"{a}")