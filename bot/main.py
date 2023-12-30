#!/usr/bin/env python

import telebot
from constants import TELEGRAM_BOT_TOKEN
import handlers

def main():
    bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

    # Setup handlers
    handlers.setup_handlers(bot)

    # Polling
    bot.polling()

if __name__ == "__main__":
    main()



