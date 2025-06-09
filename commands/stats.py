from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.helpers import get_stat

def stats_markup():
    keyboard = [
        [InlineKeyboardButton("🔙 Back", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stats = get_stat()

    if not stats:
        text = "📊 No stats recorded yet."
    else:
        text = "📊 Command Usage Stats:\n\n"
        for command, count in stats.items():
            text += f"• {command} — {count} times\n"

    await update.callback_query.edit_message_text(text=text, reply_markup=stats_markup())
