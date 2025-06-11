from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from utils.helpers import update_stat

def main_menu(update: Update, context: CallbackContext, from_query=False) -> None:
    update_stat("start")

    keyboard = [
        [InlineKeyboardButton("🟢 Ping", callback_data='ping_response')],
        [InlineKeyboardButton("📊 Stats", callback_data='stats_response')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    text = "👋 Welcome to your personal assistant bot!\n\nChoose an option below:"

    if from_query:
        update.callback_query.edit_message_text(text, reply_markup=reply_markup)
    else:
        update.message.reply_text(text, reply_markup=reply_markup)
