from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from config import BOT_TOKEN
from commands.ping import pong_response
from commands.stats import handle_stats_callback
from commands.menu import main_menu, handle_main_menu_callback

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Start command shows main menu
    app.add_handler(CommandHandler("start", main_menu))

    # Callback query handlers
    app.add_handler(CallbackQueryHandler(pong_response, pattern="^ping_response$"))
    app.add_handler(CallbackQueryHandler(handle_stats_callback, pattern="^stats_response$"))
    app.add_handler(CallbackQueryHandler(handle_main_menu_callback, pattern="^back_to_main$"))

    # Start the bot
    print("Bot is fully loaded and ready. Awaiting launch.")
    app.run_polling()

if __name__ == "__main__":
    main()
