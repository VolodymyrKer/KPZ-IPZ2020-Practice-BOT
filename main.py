from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import commands
import settings.settings_bot


def main():
    updater = Updater(settings.settings_bot.TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", commands.start))
    dp.add_handler(CommandHandler("help", commands.help))
    dp.add_handler(CommandHandler("get", commands.get))
    dp.add_handler(CommandHandler("testUpdate", commands.update))
    dp.add_handler(CommandHandler("set", commands.set))
    dp.add_handler(CommandHandler("smile", commands.smile))

    dp.add_handler(MessageHandler(Filters.text, commands.echo))
    dp.add_error_handler(commands.error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
