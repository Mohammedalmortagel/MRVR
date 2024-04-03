import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest

@app.on_message(filters.regex("^/start"), group=39)
async def start(client, message):
 if not message.chat.type == enums.ChatType.PRIVATE:
    if await joinch(message):
            return
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 nn = await get_dev_name(client, bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
  kep = ReplyKeyboardMarkup([
["مطور البوت", "مبرمج السورس"],
["السورس","اصدار"],
["اقتباس","استوري"],
["انمي","متحركه"],
["تويت", "صراحه"],
["نكته","احكام"],
[" لو خيروك","انصحني"],
["قران","نقشبندي"],
["اذكار","كتابات"],
["حروف","بوت"],
["غنيلي","سوال"],
["تلاوات","عبدالباسط"],
["افاتار بنات","افاتار شباب"]], resize_keyboard=True)
  await message.reply_text("**♪ اهلا بك ، عزيزي العضو السكر  💎 .**", reply_markup=kep,quote=True)