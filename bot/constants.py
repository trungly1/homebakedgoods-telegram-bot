import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants for the Telegram Bot
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'default_token')

# Database Constants
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', 5432))
DB_USER = os.getenv('DB_USER', 'username')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'database_name')

# Other Application Constants
MAX_ITEM_QUANTITY = int(os.getenv('MAX_ITEM_QUANTITY', 100))
DEFAULT_SHIPPING_COST = float(os.getenv('DEFAULT_SHIPPING_COST', 5.00))
SPECIAL_DISCOUNT_CODE = os.getenv('SPECIAL_DISCOUNT_CODE', 'BAKEDGOODS20')
