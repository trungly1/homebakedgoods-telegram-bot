import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler
from constants import TELEGRAM_BOT_TOKEN
from dotenv import load_dotenv

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! Welcome to the Home Baked Goods Bot!')

def main():
    """Start the bot."""
    # Load environment variables from .env file
    load_dotenv()

    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)  # Pass use_context=True

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register a command handler
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT.
    updater.idle()

if __name__ == '__main__':
    main()