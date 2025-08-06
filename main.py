import os
import time
from dotenv import load_dotenv
from telegram import Bot
from utils.indicator_logic import get_signal
from utils.telegram_format import format_signal_message

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TELEGRAM_TOKEN)

def scan_market(pair, timeframe):
    signal = get_signal(pair, timeframe)
    if signal:
        message = format_signal_message(signal)
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="HTML")

if __name__ == "__main__":
    pairs = ["EURUSD", "GBPUSD", "USDJPY"]
    timeframes = ["M1", "M2", "M5"]

    while True:
        for pair in pairs:
            for tf in timeframes:
                scan_market(pair, tf)
        time.sleep(60)
