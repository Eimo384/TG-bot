from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from utils.helpers import update_stat
from commands.menu import main_menu

def ping_command(update: Update, context: CallbackContext) -> None:
    update_stat("ping")

    keyboard = [
        [InlineKeyboardButton("🏓 Pong", callback_data='pong_response')],
        [InlineKeyboardButton("🔙 Back", callback_data='back_to_main')],
        [InlineKeyboardButton("📡 Ping", callback_data="ping_response")],
        [InlineKeyboardButton("📊 Stats", callback_data="stats_response")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Ping received! Choose an action:", reply_markup=reply_markup)

def handle_ping_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data
    query.answer()

    if data == "pong_response":
        query.edit_message_text("🏓 Pong! That was fast.")
    elif data == "back_to_main":
        main_menu(update, context, from_query=True)

