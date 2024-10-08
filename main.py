import logging
import signal
import asyncio
from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config
from telegram_bot.bot import run_telegram_bot, start_bot_thread
from restapi.routes import router as main_router
from restapi.routes import router as api_router

from config import API_HOST, API_PORT
from utils.logger import CustomLogger

# Настройка логирования
logger = CustomLogger("MyApp", "app.log", "INFO", False).get_logger()

# Флаг для завершения
shutdown_event = asyncio.Event()

# Создание экземпляра FastAPI
app = FastAPI()
app.include_router(main_router)

app.include_router(api_router)

async def start_hypercorn():
    """Запуск FastAPI с Hypercorn."""
    try:
        logger.info(f"Starting FastAPI with Hypercorn on {API_HOST}:{API_PORT}")
        config = Config()
        config.bind = [f"{API_HOST}:{API_PORT}"]
        await serve(app, config)
    except Exception as e:
        logger.error(f"Error while starting Hypercorn: {e}")
        raise

def signal_handler(sig, frame):
    """Обработчик сигнала прерывания (Ctrl+C)."""
    logger.info("Received shutdown signal. Shutting down...")
    shutdown_event.set()

signal.signal(signal.SIGINT, signal_handler)

# Основной запуск приложения
async def main():
    """Основной блок запуска приложения."""
    # Запускаем Telegram-бота в отдельном потоке
    await start_bot_thread()

    # Запускаем FastAPI сервер
    await start_hypercorn()

if __name__ == "__main__":
    """Запускаем основной цикл событий."""
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        if shutdown_event.is_set():
            logger.info("Application has been shut down.")
