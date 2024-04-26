import asyncio
import os
from pyrogram.types import CallbackQuery
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AarohiX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(filters.command(["الاوامر"], ""))
async def almortagel_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7899c7987cee4c1287963.jpg",
        caption=f"""**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس همس \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ", url=f"https://t.me/botatiiii"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("gr"))
async def almortagel_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**
★¦ اهلا بك عزيزي في قسم اوامر التشغيل في الجروبات
★¦ تشغيل + اسم السورة
★¦ فديو + اسم السورة
★¦ cvplay + اسم السورة للتشغيل بالقناة
★¦ vplay + اسم السورة لتشغيل فيديو الاذاعه
★¦ لإيقاف السورة اكتب ( ايقاف )
★¦ اكتب ( تخطي ) عشان تقلب علي الي بعدو
★¦ يوتيوب او تنزيل  + اسم السورة 
★¦ كتم+ الغاء كتم+ مسح المكتومين
★¦ طرد
= = = = = = = = = = = = = = = = = = = = = = = = = =
★¦ اكتب
★¦ اذكار 
★¦ تفعيل الاذان لتشغيل الاذن 
★¦ اكتب عبدالباسط هيجبلك سورة بصوت الشيخ عبدالباسط 
= = = = = = = = = = = = = = = = = = = = = = = = = =
★¦ اكتب ( مطورين ) لظهور مطورين السورس
★¦ اكتب ( همس ) لظهور المطورة همس 

**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="ch"), 
                    
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("ch"))
async def almortagel_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**
★¦ اهلا بك عزيزي في قسم اوامر التشغيل في القنوات
★¦ تشغيل + اسم السورة
★¦ play + اسم السورة
★¦ لايقاف الاغاني اكتب ( ايقاف )
★¦ اكتب ( تخطي ) عشان تتخطي السورة
**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="adm"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="gr"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("adm"))
async def almortagel_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**
★¦ اهلا بك عزيزي في قسم اوامر تشغيل الادمن
★¦ رفع ثانوي
★¦ تنزيل ثانوي
★¦ قائمة الثانويين
★¦ رفع ادمن
★¦ تنزيل ادمن
★¦ قائمة الادمن
★¦ حظر
★¦ الغاء الحظر
★¦ المحظورين
★¦ حظر عام
★¦ الغاء الحظر العام
★¦ المحظورين عام
★¦ اونلاين
★¦ اذاعه
★¦ تحديث
★¦ logger
★¦ ريلود
★¦ وقف
★¦ كمل
★¦ اسكت
★¦ اتكلم
★¦ ايقاف
★¦ تخطي
★¦ @all
★¦ all stop
★¦ يوتيوب / تنزيل
★¦ playing
★¦ القائمه
★¦ حذف القائمه
★¦ تحديث
★¦ الاحصائيات
★¦ لايف
★¦ مساعده
★¦ الاعدادت
★¦ بينج

** 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 **""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="gr"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def almortagel_back(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7899c7987cee4c1287963.jpg",
        caption=f"""**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس همس \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ", url=f"https://t.me/botatiiii"),
                ],

            ]

        ),

    )

