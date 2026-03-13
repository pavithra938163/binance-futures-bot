import argparse
from bot.client import get_client
from bot.trading import TradingBot
from bot.logger import logger


def validate_side(side):
    side = side.upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side


def validate_type(order_type):
    order_type = order_type.upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type


def main():

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT order")

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_type(args.type)
        quantity = args.quantity
        price = args.price

        if order_type == "LIMIT" and price is None:
            raise ValueError("LIMIT orders require --price")

        client = get_client()
        bot = TradingBot(client)

        print("\n===== Order Request =====")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        if order_type == "MARKET":
            response = bot.place_market_order(symbol, side, quantity)

        else:
            response = bot.place_limit_order(symbol, side, quantity, price)

        print("\n===== Order Response =====")

        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        print("\n✅ Order placed successfully")

    except Exception as e:

        print("\n❌ Order failed:", str(e))
        logger.error(f"Order failed: {e}")


if __name__ == "__main__":
    main()
