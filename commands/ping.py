from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from utils.helpers import update_stat

def ping_command(update: Update, context: CallbackContext) -> None:
    update_stat("ping")

    keyboard = [
        [InlineKeyboardButton("🏓 Pong", callback_data='pong_response')],
        [InlineKeyboardButton("🔙 Back", callback_data='back_to_main')]
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
        query.edit_message_text("🔙 Returning to main menu... (not yet implemented)")
