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
["اخفاء الكيبورد ⚒️"]], resize_keyboard=True)
return await message.reply_text("**♪ اهلا بك ، عزيزي المطور الاساسي  💎 .**", reply_markup=kep,quote=True)