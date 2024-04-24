import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
from random import  choice, randint

#          
                
@app.on_message(
    filters.command(["المبرمج","همس","مبرمج السورس","المطورة همس"], "")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/891a235a9f5c0ca81becf.jpg",
        caption=f"""**⩹━★⊷━⌞ ѕᴏụʀᴄᴇ ʜᴍѕ ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم المبرمج\nللتحدث مع مبرمج السورس اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ ѕᴏụʀᴄᴇ ʜᴍѕ ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᯓ 𓆩 ˹ ˛َِ ٰ𝖍𝑚ƨ 𓃠𓆃", url=f"https://t.me/hms_01"), 
                 ],[
                   InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ʜᴍѕ ⌝⚡", url=f"https://t.me/botatiiii"),
                ],

            ]

        ),

    )
