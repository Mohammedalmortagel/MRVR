import asyncio
from pyrogram import Client, filters
from AarohiX.utils.decorators import AdminRightsCheck
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX.misc import SUDOERS
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram,
                        YouTube, app)
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
                        
@app.on_message(
    command(["/command_sudo", "/command", "♕رجوع♕"])
    )
async def khalid(client: Client, message: Message):
    if message.from_user.id in SUDOERS:
       await message.reply_text(
                "اهلا عزيزي المطور\nاليك لوحة التحكم الخاصة بالبوت",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["تفعيل التواصل", "/broadcast", "حالة التواصل"],
                        ["ضع قناة الاشتراك", "حذف قناة الاشتراك"],
                        ["اذاعة للمطورين", "اذاعة للأساسيين", "اذاعة للقنوات"],
                        ["اذاعة للكل",],
                        ["الاوامر","الاحصائيات"],
                        ["حذف حساب مساعد","اضف حساب مساعد"],
                        ["المحظورين عام","مطور البوت"],
                    ],
                    resize_keyboard=True
                )
            )
    else:
       await message.reply_text(
                "اهلا عزيزي العضو\nاليك لوحة التحكم الخاصة بالبوت",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["سورس"],
                        ["الاوامر","الالعاب"],        
                    ],
                    resize_keyboard=True
                )
            )     

@app.on_message(
    command(["الاوامر"])
    )
async def khalid(client: Client, message: Message):
    if message.from_user.id in SUDOERS:
       await message.reply_text(
                "اليك اوامر البوت عزيزي المطور",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["اوامر 1","اوامر 2"],
                        ["اوامر 3","اوامر 4"],
                        ["اوامر 5","اوامر 6"],
                        ["♕رجوع♕"],
                    ],
                    resize_keyboard=True
                )
            )
    else:
       await message.reply_text(
                "اليك اوامر البوت عزيزي العضو",
                reply_markup=ReplyKeyboardMarkup(
                    [
                        ["اوامر 1","اوامر 2"],
                        ["اوامر 3","اوامر 4"],
                        ["اوامر 5"],
                        ["♕رجوع♕"],
                    ],
                    resize_keyboard=True
                )
            )  
               


txt = ["""✅**<u>اوامر الادمن:</u>**

▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬
🎧 | - إليك اوامر التحكم بالمقاطع المشغله ( دآخل المجموعات )  •
🔻 | - الاوامر تعمل بدون استخدام اي علامات  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬

◍ -『 **وقف** 』\n لإيقاف المقطع مؤقتآ داخل المحادثه الصوتيه  •
◍ -『 **كمل** 』\n لاستئناف المقطع مره اخري داخل المحادثه الصوتيه  •
◍ -『 **اسكت** 』\n لكتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **اتكلم** 』\n لألغاء كتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **تخطي** 』\n للتخطي إلي المقطع المنتظر بقائمة الانتظار لديك  •
◍ -『 **ايقاف** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬
🎙️ | - إليك اوامر التحكم بالمقاطع المشغله ( دآخل القنوات )  •
🔻 | - الاوامر تعمل بدون استخدام اي علامات  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬

◍ -『 **وقف** 』\n لإيقاف المقطع مؤقتآ داخل المحادثه الصوتيه  •
◍ -『 **كمل** 』\n لاستئناف المقطع مره اخري داخل المحادثه الصوتيه  •
◍ -『 **اسكت** 』\n لكتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **اتكلم** 』\n لألغاء كتم صوت المقطع داخل المحادثه الصوتيه  •
◍ -『 **تخطي** 』\n للتخطي إلي المقطع المنتظر بقائمة الانتظار لديك  •
◍ -『 **ايقاف** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬"""
]

@app.on_message(filters.command(["اوامر 1"], ""), group=73)

async def caesar(client: Client, message: Message):

      a = random.choice(txt)

      await message.reply(

        f"{a}")
        
        
thxt = ["""✅<u>**اوامرالتشغيل :**</u>

🎺 | - اوامر تشغيل البوت في الجروبات والقنوات  •
🎺 | - الاوامر تعمل بدون استخدام اي علامات  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬
◍ - اوامر تشغيل البوت في المجموعات - √

◍ -『 **تشغيل** 』\n ثم اسم المقطع الصوتي او الرابط الخاص به  •
◍ -『 **فيديو** 』\n ثم اسم مقطع الفيديو او الرابط الخاص به  •
◍ -『 **تنزيل** 』\n ثم اسم المقطع المراد تنزيله من موقع اليوتيوب مباشر او الرابط الخاص به  •
◍ -『 **ريلود** 』\n قم بأرسالها ( دآخل المجموعات ) لتحديث قائمه المشرفين بمجموعتك  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬
◍ - **جزء القنوات** - √
◍ - اوامر تشغيل البوت في القنوات 👇 - √

◍ -『 **تشغيل** 』\n ثم اسم المقطع الصوتي او الرابط الخاص به لتشغيله بقناتك  •
◍ -『 **فيديو** 』\nثم اسم الفيديو او الرابط الخاص به لتشغيله بقناتك  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬."""]
        
@app.on_message(filters.command(["اوامر 2"], ""), group=173)

async def caesar(client: Client, message: Message):

      a = random.choice(thxt)

      await message.reply(

        f"{a}")        
        
htt = ["""✅<u>**اوامر البوت:**</u>

▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬
✅ | - إليك قسم ( الاوامر الاضافيه ) للبوت  •
✅ | - جميع الاوامر تعمل بدون علامات  •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬

◍ -『 **حدد** 』\n ثم رقم المجموعات الذي تستخدم بوتك فيديو بنفس الوقت •

◍ -『 **وضع شغل** 』\n لضبط وضع تحكم التشغيل للأدمن او للاعضاء داخل مجموعتك  •

◍ -『 **القائمه** 』\n لعرض قائمه التشغيل الخاصه بك  •

◍ -『 **حذف القائمه** 』\n لحذف قائمه التشغيل الخاصه بك  •

◍ -『 **لغه** 』\n لتغيير لغة البوت إلي اي لغه اخري  •

◍ -『 **احصائيات** 』\n لعرض قسم الاحصائيات العامه للبوت ولترند التشغيل العالمي •

◍ -『 **ريلود** 』\n لتحديث قائمة المشرفين داخل مجموعتك •

◍ -『 **بينج** 』\n لقياس سرعه التشغيل علي السيرفر وعرض تفاصيل معلومات التشغيل •

◍ -『 **كلمات** 』\n ثم اسم الاغنيه لجلب كلمات الاغنيه كامله بصيغه النصوص •

◍ -『 **تنزيل** 』\n ثم اسم المقطع او الرابط الخاص به لتحميله مباشر من اليوتيوب •
▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬"""]

@app.on_message(filters.command(["اوامر 3"], ""), group=373)

async def caesar(client: Client, message: Message):

      a = random.choice(htt)

      await message.reply(

        f"{a}")   
        
htxt = ["""😜 **<u>ᴀᴜᴛʜ ᴜsᴇʀs :</u>**
ᴀᴜᴛʜ ᴜsᴇʀs ᴄᴀɴ ᴜsᴇ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ. [ᴀᴅᴍɪɴs ᴏɴʟʏ]

/auth [ᴜsᴇʀɴᴀᴍᴇ] : ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜ ʟɪsᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.

/unauth [ᴜsᴇʀɴᴀᴍᴇ] : ʀᴇᴍᴏᴠᴇ ᴀ ᴀᴜᴛʜ ᴜsᴇʀs ғʀᴏᴍ ᴛʜᴇ ᴀᴜᴛʜ ᴜsᴇʀs ʟɪsᴛ.

/authusers : sʜᴏᴡs ᴛʜᴇ ᴀᴜᴛʜ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ."""
        ]

@app.on_message(filters.command(["اوامر 4"], ""), group=273)

async def caesar(client: Client, message: Message):

      a = random.choice(htxt)

      await message.reply(

        f"{a}")           
        
htx = ["""🍒 **<u>ʙʀᴏᴀᴅᴄᴀsᴛ ғᴇᴀᴛᴜʀᴇ</u>** [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :

/broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.

<u>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴍᴏᴅᴇs:</u>
**-pin** : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.
**-pinloud** : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴀɴᴅ sᴇɴᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴍᴇᴍʙᴇʀs.
**-user** : ʙʀᴏᴀᴅᴄᴀsᴛs ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.
**-assistant** : ʙʀᴏᴀᴅᴄᴀsᴛ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀssɪᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.
**-nobot** : ғᴏʀᴄᴇs ᴛʜᴇ ʙᴏᴛ ᴛᴏ ɴᴏᴛ ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ..

**ᴇxᴀᴍᴩʟᴇ:** `/broadcast -user -assistant -pin ᴛᴇsᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ`
"""
        ]

@app.on_message(filters.command(["اوامر 5"], ""), group=253)

async def caesar(client: Client, message: Message):

      a = random.choice(htx)

      await message.reply(

        f"{a}")          