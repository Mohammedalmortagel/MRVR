import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from AarohiX.misc import SUDOERS
from AarohiX import app

admin_keyboard = ReplyKeyboardMarkup([
    ['تفعيل التواصل', '/broadcast', 'حالة التواصل'],
    ['ضع قناة الاشتراك', 'حذف قناة الاشتراك'],
    ['اذاعة للمطورين', 'اذاعة للأساسيين', 'اذاعة للقنوات'],
    ['اذاعة للكل', 'توجيه للكل'],
    ['توجيه للمستخدمين', 'توجيه للجروبات', 'توجيه للقنوات'],
    ['اخفاء الكيبورد ⚒️']
], resize_keyboard=True)

# دالة للتعامل مع أمر /admin
@app.on_message(filters.command("/start") &  filters.private & SUDOERS)
async def admin(client, message):
    await message.reply("لوحة المفاتيح الخاصة بالمطور", reply_markup=admin_keyboard)
    
@app.on_message(filters.command("اخفاء الكيبورد ⚒️") & filters.private & SUDOERS)
async def admin(client, message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )
# دالة للتعامل مع الأوامر الأخرى

