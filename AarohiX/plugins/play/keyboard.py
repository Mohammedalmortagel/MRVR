import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

admin_keyboard = ReplyKeyboardMarkup([
    ['تفعيل التواصل', '/broadcast', 'حالة التواصل'],
    ['ضع قناة الاشتراك', 'حذف قناة الاشتراك'],
    ['اذاعة للمطورين', 'اذاعة للأساسيين', 'اذاعة للقنوات'],
    ['اذاعة للكل', 'توجيه للكل'],
    ['توجيه للمستخدمين', 'توجيه للجروبات', 'توجيه للقنوات'],
    ['اخفاء الكيبورد ⚒️']
], resize_keyboard=True)

# دالة للتعامل مع أمر /admin
@app.on_message(filters.regex("^/start"))
async def cpanel(_, message: Message): 
    await message.reply("لوحة المفاتيح الخاصة بالمطور", reply_markup=admin_keyboard)

# دالة للتعامل مع الأوامر الأخرى
@app.on_message(filters.text & ~filters.command("اخفاء الكيبورد ⚒️") & filters.private & SUDOERS)
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )
    pass
