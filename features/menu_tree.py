from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🤖 AI & Chat", callback_data="menu_ai")],
        [InlineKeyboardButton("⬇️ Downloaders", callback_data="menu_download")],
        [InlineKeyboardButton("🎧 Audio Tools", callback_data="menu_audio")],
        [InlineKeyboardButton("🕵️ OSINT Tools", callback_data="menu_osint")],
        [InlineKeyboardButton("🔍 Search Tools", callback_data="menu_search")],
        [InlineKeyboardButton("🎮 Fun & Games", callback_data="menu_fun")],
        [InlineKeyboardButton("📊 Stats", callback_data="stats_response")],
    ]
    return InlineKeyboardMarkup(keyboard)
