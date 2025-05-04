import telebot
import json
import os

# الحصول على التوكن من المتغير البيئي
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# تحميل الرتب من ملف JSON
def load_ranks():
    try:
        with open("ranks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# وظيفة التحقق من العضو
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً! كيف يمكنني مساعدتك؟")

# إضافة أو تعديل رتبة
@bot.message_handler(commands=['add_rank'])
def add_rank(message):
    ranks = load_ranks()
    args = message.text.split()
    if len(args) == 3:
        username = args[1]
        rank = args[2]
        ranks[username] = rank
        with open("ranks.json", "w") as file:
            json.dump(ranks, file)
        bot.reply_to(message, f"تم إضافة الرتبة '{rank}' لـ @{username}")
    else:
        bot.reply_to(message, "يرجى استخدام الصيغة الصحيحة: /add_rank @username rank")

# وظيفة كتم أو طرد
@bot.message_handler(commands=['mute'])
def mute_user(message):
    args = message.text.split()
    if len(args) == 2:
        username = args[1]
        bot.reply_to(message, f"تم كتم المستخدم @{username}")

@bot.message_handler(commands=['kick'])
def kick_user(message):
    args = message.text.split()
    if len(args) == 2:
        username = args[1]
        bot.reply_to(message, f"تم طرد المستخدم @{username}")

# بدء البوت
if __name__ == "__main__":
    bot.polling()
