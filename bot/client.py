from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL
from bot.logger import logger

def get_client():
    try:
        client = Client(API_KEY, API_SECRET)
        client.FUTURES_URL = BASE_URL

        logger.info("Connected to Binance Futures Testnet")
        return client

    except Exception as e:
        logger.error(f"Connection failed: {e}")
        raise
