import logging
from dotenv import dotenv_values

import telegram as tg
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from handlers import start_command, help_command, register_neighbour_command, echo


API_TOKEN = dotenv_values(".env")['API_TOKEN']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logging.info('Connected bot: @%s' % tg.Bot(API_TOKEN).get_me()['username'])

    updater = Updater(API_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("register_neighbour", register_neighbour_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
