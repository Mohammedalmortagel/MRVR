import asyncio
from pyrogram import Client, filters
from AarohiX.utils.decorators import AdminRightsCheck
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX.misc import SUDOERS
from strings.filters import command
from config import OWNER_ID
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram,YouTube, app)
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardRemove, ReplyKeyboardMarkup     

@app.on_message(command(["الاوامر"]))
async def khalid(client: Client, message: Message):
       await message.reply_photo(photo=f"https://te.legra.ph/file/7899c7987cee4c1287963.jpg",
        caption=f"""**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس همس \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**""", reply_markup=ReplyKeyboardMarkup(
                    [
                        ["اوامر 1","اوامر 2"],
                        ["اوامر 3","المطور"],
                        ["❎ ¦ حذف الاوامر"], 
                    ],
                    resize_keyboard=True)
               
@app.on_message(filters.text, group=39)
async def almortagel(client, message):
   if message.text == "اوامر 1":
       await message.reply_text(f""""**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**
★¦ اهلا عزيزي في قسم التشغيل في الجروبات
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

[**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**](https://t.me/botatiiii)""")
   elif message.text == "اوامر 2":
       await message.reply_text(f"""**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**
★¦ اهلا عزيزي في قسم التشغيل في القنوات
★¦ تشغيل + اسم السورة
★¦ play + اسم السورة
★¦ لايقاف الاغاني اكتب ( ايقاف )
★¦ اكتب ( تخطي ) عشان تتخطي السورة
[**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**](https://t.me/botatiiii)""")
   elif message.text ==  "اوامر 3":
       await message.reply_text(f="""**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**
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

[**⩹━⊷⌯⌞ 𖧊 ѕᴏụʀᴄᴇ ʜᴍѕ 𖧊 ⌝⌯⊶━⩺**](https://t.me/botatiiii)""")

@app.on_message(filters.command(["❎ ¦ حذف الاوامر"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الاوامر بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )