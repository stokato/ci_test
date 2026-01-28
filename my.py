from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env

# Теперь можно получить их
secret_key = os.getenv("SECRET_KEY")
debug_mode = os.getenv("DEBUG")
