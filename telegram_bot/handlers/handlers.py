# telegram_bot/handlers.py

import requests
import telebot
from telebot import types
from config import API_HOST, API_PORT


def register_handlers(telegram_bot: telebot.TeleBot):
    @telegram_bot.message_handler(commands=['start'])
    def start(message: types.Message):
        telegram_bot.reply_to(message, "Привет! Я ваш Telegram бот.")

    @telegram_bot.message_handler(commands=['help'])
    def help_command(message: types.Message):
        telegram_bot.reply_to(message, "Это помощь по командам бота.")
        
    @telegram_bot.message_handler(commands=['health'])
    def health_check(message: types.Message):
        try:
            response = requests.get(f"http://127.0.0.1:{API_PORT}/health")
            if response.status_code == 200:
                telegram_bot.reply_to(message, "Сервер работает нормально!")
            else:
                telegram_bot.reply_to(message, "Сервер не отвечает.")
        except Exception as e:
            telegram_bot.reply_to(message, f"Ошибка при проверке состояния: {str(e)}")