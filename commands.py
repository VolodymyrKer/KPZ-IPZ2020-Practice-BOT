import logging

from coinbase.factorio_spaghetti import get_prices
from settings.enum_coins import Coins

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi!')


def help(update, context):
    update.message.reply_text("Commands: /get [coin] - get [coin] prices\n"
                              "Coins: BTC, ETH, MATIC, SOL")


def echo(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def get(update, context):
    update.message.reply_text(get_prices(Coins[context.args[0].upper()]))