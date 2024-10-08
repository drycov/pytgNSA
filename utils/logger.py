import logging
import os
from logging.handlers import RotatingFileHandler

class CustomLogger:
    def __init__(self, app_type: str, log_filename: str, log_level: str = "INFO", console_output: bool = True):
        """
        Инициализация логгера.

        :param app_type: Тип приложения (имя логгера)
        :param log_filename: Имя файла для логов
        :param log_level: Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        :param console_output: Выводить ли логи в консоль
        """
        self.app_type = app_type
        self.log_filename = log_filename
        self.log_level = log_level.upper()
        self.console_output = console_output
        self.logger = logging.getLogger(self.app_type)
        self.setup_logger()

    def setup_logger(self):
        """Настройка логгера: создание директории, установка обработчиков и формата логов."""
        # Создаем директорию для логов, если ее нет
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Полный путь к файлу логов
        log_file = os.path.join(log_dir, self.log_filename)

        # Устанавливаем уровень логирования
        self.logger.setLevel(self.get_log_level())

        # Создаем обработчик для записи логов в файл
        file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
        file_handler.setFormatter(self.get_formatter())
        self.logger.addHandler(file_handler)

        # Если нужно вывести в консоль, добавляем консольный обработчик
        if self.console_output:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.get_formatter())
            self.logger.addHandler(console_handler)

    def get_log_level(self):
        """Получение уровня логирования."""
        levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }
        return levels.get(self.log_level, logging.INFO)

    def get_formatter(self):
        """Создание форматтера для логов."""
        return logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def get_logger(self):
        """Возвращает настроенный объект логгера."""
        return self.logger

# Пример использования
if __name__ == "__main__":
    app_logger = CustomLogger(
        app_type="MyApp",           # Тип приложения
        log_filename="myapp.log",   # Имя файла для логов
        log_level="DEBUG",          # Уровень логирования
        console_output=True         # Включение вывода в консоль
    ).get_logger()

    # Тестирование логирования
    app_logger.info("This is an info message")
    app_logger.debug("This is a debug message")
    app_logger.warning("This is a warning message")
    app_logger.error("This is an error message")
