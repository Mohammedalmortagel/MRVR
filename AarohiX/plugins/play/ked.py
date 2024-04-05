import pyrogram
from pyrogram import Client, filters
from config import BANNED_USERS, OWNER_ID 
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from AarohiX.misc import SUDOERS
from AarohiX import app


@Client.on_message(filters.command(["/start","رجوع للقائمة الرئيسيه"], ""))
async def start(client, message):
 if not message.chat.type == enums.ChatType.PRIVATE:
    if await joinch(message):
            return
 bot_username = client.me.username
 dev = await get_dev(bot_username)
 nn = await get_dev_name(client, bot_username)
 if message.chat.id == dev or message.chat.username in OWNER:
   kep = ReplyKeyboardMarkup([
["تفعيل التواصل", "/broadcast", "حالة التواصل"],
["ضع قناة الاشتراك", "حذف قناة الاشتراك"],
["اذاعة للمطورين", "اذاعة للأساسيين", "اذاعة للقنوات"],
["اذاعة للكل", "توجيه للكل"],
["توجيه للمستخدمين", "توجيه للجروبات", "توجيه للقنوات"],
["اخفاء الكيبورد ⚒️"]],resize_keyboard=True)
 await message.reply("لوحة المفاتيح الخاصة بالمطور", reply_markup=keyboard,quote=True)

@app.on_message(filters.command("اخفاء الكيبورد ⚒️") & filters.private & SUDOERS)
async def admin(client, message):
  await message.reply("❎ ¦ تم حذف الكيبورد بنجاح",quote=True,reply_markup=ReplyKeyboardRemove(selective=True))