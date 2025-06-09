from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import BOT_TOKEN
import logging
import asyncio
import os

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Global stats (to be moved to JSON later)
from utils.helpers import update_stat, get_stat

# Start command (main menu)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    update_stat("start")
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("🟢 Ping", callback_data="cmd_ping"),
        InlineKeyboardButton("📊 Stats", callback_data="cmd_stats")
    )
    await message.answer("👋 Welcome to your personal assistant bot!\n\nChoose an option below:", reply_markup=keyboard)

# Handle inline buttons
@dp.callback_query_handler(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data

    if data == "cmd_ping":
        from commands.ping import ping_command
        await ping_command(callback_query.message, callback_query.from_user)
    elif data == "cmd_stats":
        stats = get_stat()
        text = "📊 Command Usage Stats:\n"
        for k, v in stats.items():
            text += f"• {k} – {v} times\n"
        await callback_query.message.edit_text(text, reply_markup=back_to_menu())
    elif data == "cmd_back":
        await send_welcome(callback_query.message)

# Back to menu button
def back_to_menu():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔙 Back", callback_data="cmd_back"))
    return keyboard

# Logging
logging.basicConfig(level=logging.INFO)

# Run bot
if __name__ == '__main__':
    from utils.helpers import ensure_stat_file
    ensure_stat_file()
    executor.start_polling(dp, skip_updates=True)
