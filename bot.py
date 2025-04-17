from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("""
      This is only a test script to see if the bot is working with the genrated token
     """)

TOKEN = '7926957867:AAEqoVnKPlFhDlX_Yjop_smD9x86zdhyeXo'


def start(update, context):
    update.message.reply_text("Hi! I'm your bot.")


def echo(update, context):
    update.message.reply_text(f"You said: {update.message.text}")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
