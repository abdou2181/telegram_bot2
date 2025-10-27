import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("💫 Donate 1 Star", callback_data="donate_1"),
        telebot.types.InlineKeyboardButton("🌟 Donate 10 Stars", callback_data="donate_10"),
        telebot.types.InlineKeyboardButton("✨ Donate 100 Stars", callback_data="donate_100"),
    )
    markup.add(telebot.types.InlineKeyboardButton("🪙 Custom Amount", callback_data="donate_custom"))
    bot.send_message(message.chat.id, "Welcome! Choose an amount to donate 💖", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("donate"))
def handle_donation(call):
    amount = call.data.split("_")[1]
    bot.answer_callback_query(call.id, f"You selected to donate {amount} Stars 💫")
    bot.send_message(call.message.chat.id, f"Thanks for donating {amount} Stars!")

print("🤖 Bot is running...")
bot.infinity_polling()
