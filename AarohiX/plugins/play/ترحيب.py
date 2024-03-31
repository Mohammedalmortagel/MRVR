import asyncio
import random
from AarohiX.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from AarohiX import app
from config import *


almortagel_responses = [
    "- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه\n\nوبدون تهنيج او تقطيع او توقف وكمان ان البوت في مميزات جامدة⚡️♥️.\n\nارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ⚡️♥️\n\nمعرف البوت 🎸 [ {bot_username} ]\n\n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤e 𝘤𝘩𝘢𝘵 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ {bot_username}"
       
]

@app.on_message(filters.command(["ترند"], ""), group=39)
async def almortagel_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(almortagel_responses)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])

    await message.reply(
        f"{bar}",
        reply_markup=keyboard
    )