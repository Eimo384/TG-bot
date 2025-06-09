from commands.stats import stats_command
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import BOT_TOKEN
from commands.ping import start_command, pong_response, back_to_main

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command
    app.add_handler(CommandHandler("start", start_command))

    # Register callback query handlers
    app.add_handler(CallbackQueryHandler(pong_response, pattern="^ping_response$"))
    app.add_handler(CallbackQueryHandler(back_to_main, pattern="^back_to_main$"))
    app.add_handler(CallbackQueryHandler(stats_command, pattern="^stats_response$"))

    # Start the bot
    print("Bot is fully loaded and ready. Awaiting launch.")
    app.run_polling()

if __name__ == "__main__":
    main()
