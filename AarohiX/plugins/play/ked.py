import asyncio
from pyrogram import Client, filters
from AarohiX.utils.decorators import AdminRightsCheck
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AarohiX.misc import SUDOERS
from AarohiX import (Apple, Resso, SoundCloud, Spotify, Telegram,YouTube, app)
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
                        
@app.on_message(filters.command("^/start", "♕رجوع♕"), group=39)
async def cpanel(_, message: Message):
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
                        ["افاتار بنات","افاتار شباب"],
                        ["❎ ¦ حذف الكيبورد"]      
                    ],
                    resize_keyboard=True
                )
            )     

@app.on_message(filters.command(["الاوامر"], ""))
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
               
@app.on_message(filters.text, group=39)
async def almortagel(client, message):
   if message.text == "اوامر 1":
       await message.reply_text(f"✅**اوامر الادمن**\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n🎧 | - إليك اوامر التحكم بالمقاطع المشغله ( دآخل المجموعات )  •\n🔻 | - الاوامر تعمل بدون استخدام اي علامات  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ -『 **وقف** 』\n لإيقاف المقطع مؤقتآ داخل المحادثه الصوتيه  •\n◍ -『 **كمل** 』\n لاستئناف المقطع مره اخري داخل المحادثه الصوتيه  •\n◍ -『 **اسكت** 』\n لكتم صوت المقطع داخل المحادثه الصوتيه  •\n◍ -『 **اتكلم** 』\n لألغاء كتم صوت المقطع داخل المحادثه الصوتيه  •\n◍ -『 **تخطي** 』\n للتخطي إلي المقطع المنتظر بقائمة الانتظار لديك  •\n◍ -『 **ايقاف** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n🎙️ | - إليك اوامر التحكم بالمقاطع المشغله ( دآخل القنوات )  •\n🔻 | - الاوامر تعمل بدون استخدام اي علامات  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ -『 **وقف** 』\n لإيقاف المقطع مؤقتآ داخل المحادثه الصوتيه  •\n◍ -『 **كمل** 』\n لاستئناف المقطع مره اخري داخل المحادثه الصوتيه  •\n◍ -『 **اسكت** 』\n لكتم صوت المقطع داخل المحادثه الصوتيه  •\n◍ -『 **اتكلم** 』\n لألغاء كتم صوت المقطع داخل المحادثه الصوتيه  •\n◍ -『 **تخطي** 』\n للتخطي إلي المقطع المنتظر بقائمة الانتظار لديك  •\n◍ -『 **ايقاف** 』\n لأنهاء التشغيل ومغادره المساعد المحادثه الصوتيه  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬")
   elif message.text == "اوامر 2":
       await message.reply_text(f"✅<u>**اوامرالتشغيل :**</u>\n🎺 | - اوامر تشغيل البوت في الجروبات والقنوات  •\n🎺 | - الاوامر تعمل بدون استخدام اي علامات  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ - اوامر تشغيل البوت في المجموعات - √\n◍ -『 **تشغيل** 』\n ثم اسم المقطع الصوتي او الرابط الخاص به  •\n◍ -『 **فيديو** 』\n ثم اسم مقطع الفيديو او الرابط الخاص به  •\n◍ -『 **تنزيل** 』\n ثم اسم المقطع المراد تنزيله من موقع اليوتيوب مباشر او الرابط الخاص به  •\n◍ -『 **ريلود** 』\n قم بأرسالها ( دآخل المجموعات ) لتحديث قائمه المشرفين بمجموعتك  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ - **جزء القنوات** - √\n◍ - اوامر تشغيل البوت في القنوات 👇 - √\n◍ -『 **تشغيل** 』\n ثم اسم المقطع الصوتي او الرابط الخاص به لتشغيله بقناتك  •\n◍ -『 **فيديو** 』\nثم اسم الفيديو او الرابط الخاص به لتشغيله بقناتك  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬.")
   elif message.text ==  "اوامر 3":
       await message.reply_text(f"✅**اوامر البوت:**\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n✅ | - إليك قسم ( الاوامر الاضافيه ) للبوت  •\n✅ | - جميع الاوامر تعمل بدون علامات  •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬\n◍ -『 **حدد** 』\n ثم رقم المجموعات الذي تستخدم بوتك فيديو بنفس الوقت •\n◍ -『 **وضع شغل** 』\n لضبط وضع تحكم التشغيل للأدمن او للاعضاء داخل مجموعتك  •\n◍ -『 **القائمه** 』\n لعرض قائمه التشغيل الخاصه بك  •\n◍ -『 **حذف القائمه** 』\n لحذف قائمه التشغيل الخاصه بك  •\n◍ -『 **لغه** 』\n لتغيير لغة البوت إلي اي لغه اخري  •\n◍ -『 **احصائيات** 』\n لعرض قسم الاحصائيات العامه للبوت ولترند التشغيل العالمي •\n◍ -『 **ريلود** 』\n لتحديث قائمة المشرفين داخل مجموعتك •\n◍ -『 **بينج** 』\n لقياس سرعه التشغيل علي السيرفر وعرض تفاصيل معلومات التشغيل •\n◍ -『 **كلمات** 』\n ثم اسم الاغنيه لجلب كلمات الاغنيه كامله بصيغه النصوص •\n◍ -『 **تنزيل** 』\n ثم اسم المقطع او الرابط الخاص به لتحميله مباشر من اليوتيوب •\n▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬࣪▭𝅼▬")
   elif message.text == "اوامر 4":
       await message.reply_text(f"😜 **ᴀᴜᴛʜ ᴜsᴇʀs**\nᴀᴜᴛʜ ᴜsᴇʀs ᴄᴀɴ ᴜsᴇ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ɪɴ ᴛʜᴇ ᴄʜᴀᴛ. [ᴀᴅᴍɪɴs ᴏɴʟʏ]\n/auth [ᴜsᴇʀɴᴀᴍᴇ] : ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜ ʟɪsᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.\n/unauth [ᴜsᴇʀɴᴀᴍᴇ] : ʀᴇᴍᴏᴠᴇ ᴀ ᴀᴜᴛʜ ᴜsᴇʀs ғʀᴏᴍ ᴛʜᴇ ᴀᴜᴛʜ ᴜsᴇʀs ʟɪsᴛ.\n/authusers : sʜᴏᴡs ᴛʜᴇ ᴀᴜᴛʜ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.")
   elif message.text == "اوامر 5":
       await message.reply_text(f"🍒 **<u>ʙʀᴏᴀᴅᴄᴀsᴛ ғᴇᴀᴛᴜʀᴇ</u>** [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :\n/broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.\n<u>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ ᴍᴏᴅᴇs:</u>\n**-pin** : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.\n**-pinloud** : ᴩɪɴs ʏᴏᴜʀ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴀɴᴅ sᴇɴᴅ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴍᴇᴍʙᴇʀs\n**-user** : ʙʀᴏᴀᴅᴄᴀsᴛs ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴜsᴇʀs ᴡʜᴏ ʜᴀᴠᴇ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.\n**-assistant** : ʙʀᴏᴀᴅᴄᴀsᴛ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ᴛʜᴇ ᴀssɪᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴏғ ᴛʜᴇ ʙᴏᴛ.\n**-nobot** : ғᴏʀᴄᴇs ᴛʜᴇ ʙᴏᴛ ᴛᴏ ɴᴏᴛ ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ..\n**ᴇxᴀᴍᴩʟᴇ:** `/broadcast -user -assistant -pin ᴛᴇsᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ`")