from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from utils.helpers import get_stat, update_stat
from commands.menu import main_menu

def stats_command(update: Update, context: CallbackContext) -> None:
    update_stat("stats")
    stats = get_stat()

    if not stats:
        text = "📊 No stats available yet."
    else:
        text = "📊 Command Usage Stats:\n"
        for k, v in stats.items():
            text += f"• {k.capitalize()} – {v} times\n"

    keyboard = [
        [InlineKeyboardButton("🔙 Back", callback_data='back_to_main')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(text, reply_markup=reply_markup)

def handle_stats_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    stats_command(update, context)

