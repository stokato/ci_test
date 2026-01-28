from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# Загрузка переменных из .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
DEBUG = os.getenv("DEBUG") == "True"


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот.")


if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print(f"Бот запущен. DEBUG = {DEBUG}")
    app.run_polling()
