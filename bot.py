import os
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = os.getenv("AAHU9riaEtk7W0CkejSNMQDijihHrXllAF8")

def handle_message(update, context):
    user_text = update.message.text
    update.message.reply_text(f"คุณพิมพ์ว่า: {user_text}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
