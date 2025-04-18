# config.py
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("❌ Переменная окружения TOKEN не найдена!")
