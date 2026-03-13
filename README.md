# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot for Binance Futures Testnet.

## Features

- Market orders
- Limit orders
- BUY / SELL
- CLI input
- Logging
- Error handling

## Setup

1 Install dependencies

pip install -r requirements.txt

2 Create .env file

BINANCE_API_KEY=your_api_key  
BINANCE_API_SECRET=your_secret_key

3 Run bot

Example MARKET order

python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Example LIMIT order

python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Logs

Logs are stored in

logs/bot.log

## Assumptions

- Binance Futures Testnet account created
- API keys enabled
- Using python-binance library