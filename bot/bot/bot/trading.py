from bot.logger import logger


class TradingBot:

    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):

        try:
            logger.info(f"Market Order Request | {symbol} {side} {quantity}")

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Market Order Response | {order}")

            return order

        except Exception as e:
            logger.error(f"Market order failed: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):

        try:
            logger.info(
                f"Limit Order Request | {symbol} {side} qty={quantity} price={price}"
            )

            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(f"Limit Order Response | {order}")

            return order

        except Exception as e:
            logger.error(f"Limit order failed: {e}")
            raise
