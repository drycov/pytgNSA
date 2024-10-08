import os
import platform
import sys
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Определение режима работы (dev или prod)
mode = os.getenv("MODE", "dev").lower()  # Установите значение по умолчанию в dev

if len(sys.argv) > 1:
    mode = sys.argv[1].lower()

# Определяем тип ОС
is_windows = platform.system() == 'Windows'
is_linux = platform.system() == 'Linux'
is_macos = platform.system() == 'Darwin'


# Выбор токена в зависимости от режима и ОС
if mode == "prod":
    TOKEN = os.getenv("PROD_TOKEN")  # Используется PROD_TOKEN для всех ОС в продакшене
elif is_windows and mode == "dev":
    TOKEN = os.getenv("DEV_TOKEN")  # Используется DEV_TOKEN для Windows в режиме dev
elif is_linux:
    TOKEN = os.getenv("PROD_TOKEN")  # Используется PROD_TOKEN для Linux в режиме dev
elif is_macos:
    TOKEN = os.getenv("DEV_TOKEN")  # Используется DEV_TOKEN для macOS в режиме dev
else:
    TOKEN = os.getenv("DEV_TOKEN")  # По умолчанию используем DEV_TOKEN для остальных случаев

# Конфигурация приложения
APP_TYPE = os.getenv("APP_TYPE")
NOWEB = os.getenv("NOWEB")
API_PORT = os.getenv("API_PORT", "5000")
API_HOST = os.getenv("API_HOST", "0.0.0.0")

# Названия ботов
PROD_BOT_NAME = os.getenv("PROD_BOT_NAME")
DEV_BOT_NAME = os.getenv("DEV_BOT_NAME")

# Магические переменные
DEFAULT_ADMIN = os.getenv("DEFAULT_ADMIN", "6818244868")  # Значение по умолчанию
BOT_CHAT_ADMIN = os.getenv("BOT_CHAT_ADMIN", "-1002084129010")  # Магическая переменная
