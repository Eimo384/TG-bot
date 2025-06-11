from telegram import Update
from telegram.ext import CallbackContext
from features.menu_tree import main_menu_keyboard
from utils.helpers import update_stat

def main_menu(update: Update, context: CallbackContext) -> None:
    update_stat("menu")
    update.message.reply_text(
        "🤖 Welcome to your smart assistant bot!\n\nChoose a category below:",
        reply_markup=main_menu_keyboard()
    )

def handle_main_menu_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    main_menu(query, context)
