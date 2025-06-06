from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get("BOTTOKEN")

def start(update, context):
    update.message.reply_text("Bot চালু হয়েছে!")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    # এখানে start_polling() দিয়ে bot চালু করো
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
