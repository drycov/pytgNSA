import logging
import asyncio
import threading
import time
import telebot
from config import TOKEN
from .handlers import register_handlers

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание экземпляра Telegram бота
telegram_bot = telebot.TeleBot(TOKEN)

# Регистрируем обработчики команд
register_handlers(telegram_bot)

# Функция для запуска Telegram бота
def run_telegram_bot():
    """Запуск Telegram-бота в отдельном потоке."""
    while True:
        try:
            telegram_bot.polling(none_stop=True)
        except Exception as e:
            logging.error(f"Ошибка при работе с ботом: {e}")
            # Если возникла ошибка, ожидаем перед перезапуском
            time.sleep(5)

# Функция для запуска бота в отдельном потоке
async def start_bot_thread():
    """Запускаем Telegram-бота в отдельном потоке."""
    bot_thread = threading.Thread(target=run_telegram_bot)
    bot_thread.daemon = True  # Позволяет завершить поток при завершении основного приложения
    bot_thread.start()