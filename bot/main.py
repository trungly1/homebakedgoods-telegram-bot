from telegram.ext import Updater, CommandHandler
from constants import TELEGRAM_BOT_TOKEN

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Welcome to the Home Baked Goods Bot!')

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register a command handler
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT.
    updater.idle()

if __name__ == '__main__':
    main()
