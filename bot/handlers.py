def setup_handlers(bot):
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Welcome to the Home Baked Goods Bot!")

    # Add more handlers here
