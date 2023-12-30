# Home Baked Goods Telegram Bot

A Telegram bot for managing a home baked goods shop.

## Overview

This bot allows customers to browse and order baked goods through Telegram. It provides an easy way for a home baker to manage orders and communicate with customers.

## Features

- Browse menu of available baked goods
- Add items to a cart
- Checkout and pay for orders
- Receive order confirmations and updates
- Admin interface to add/edit menu items
- Notifications for new orders and messages
- Customer management

## Setup and Installation

### Prerequisites

- Telegram account and bot token
- Python 3.6+
- Required Python packages (Telepot, sqlite3, etc)

### Installation

- Clone this repository
- Install dependencies: `pip install -r requirements.txt`
- Add Telegram bot token to config.py
- Run `python bot.py` to start the bot

### Database Setup

- The bot uses a SQLite database to store order information. This will be automatically created on first run.

The database schema is described in schema.sql.

## Usage

Customers can interact with the bot by messaging @homebakedbot. The bot will present a menu and allow them to browse, add to cart, and checkout.

The admin interface allows managing menu items, viewing new orders, and messaging customers.

See the wiki for more detailed usage information.

## Contributing

Pull requests are welcome! Feel free to open issues for any bugs or desired features.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
