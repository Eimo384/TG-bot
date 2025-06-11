from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from commands.menu import main_menu

def download_menu(update: Update, context: CallbackContext, from_query=False) -> None:
    if from_query:
        query = update.callback_query
        query.answer()
        method = query.edit_message_text
    else:
        method = update.message.reply_text

    keyboard = [
        [InlineKeyboardButton("📥 YouTube Downloader", callback_data="download_youtube")],
        [InlineKeyboardButton("🌐 URL Downloader", callback_data="download_url")],
        [InlineKeyboardButton("🔙 Back", callback_data="back_to_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    method("📂 *Download Tools*\nChoose what you want to do:", reply_markup=reply_markup, parse_mode="Markdown")

def handle_download_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data
    query.answer()

    if data == "download_youtube":
        query.edit_message_text("📥 YouTube downloader not yet implemented.")
    elif data == "download_url":
        query.edit_message_text("🌐 URL downloader not yet implemented.")
    elif data == "back_to_main":
        main_menu(update, context, from_query=True)
