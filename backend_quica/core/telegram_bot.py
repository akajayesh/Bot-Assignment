from decouple import config
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")


import django
django.setup()

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from core.models import TelegramUser

def start(update: Update, context: CallbackContext):
    username = update.message.from_user.username
    TelegramUser.objects.get_or_create(username=username)
    update.message.reply_text(f"Hello @{username}! You've been registered ✅")

def main():
    updater = Updater(token=config("TELEGRAM_BOT_TOKEN"), use_context=True)  
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    print("Bot is running... Waiting for /start command")
    updater.idle()

if __name__ == '__main__':
    main()
