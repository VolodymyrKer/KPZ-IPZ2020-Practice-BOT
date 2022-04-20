
import html
import logging

import requests

from coinbase.factorio_spaghetti import get_prices
from settings.enum_coins import Coins

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi! Type /help for commands')


def help(update, context):
    update.message.reply_text("Commands: /get [coin] - get [coin] prices\n"
                              "/set [coin] [seconds] - set [coin] price with interval [seconds]\n"
                              "/smile [text] - spacebars get random emoji\n"
                              "Coins: BTC, ETH, MATIC, SOL")


def echo(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def get(update, context):
    update.message.reply_text(get_prices(Coins[context.args[0].upper()]))


def update(update, context):
    print(update)


def smile(update, context):
    text = ""
    for word in context.args:
        response_smile = requests.get("https://ranmoji.herokuapp.com/emojis/api/v.1.0/")
        data_smile = response_smile.json()
        emoji = html.unescape(data_smile.get('emoji').split(';')[0] + ';')
        text += emoji
        text += word
    update.message.reply_text(text)


def give(context):
    job = context.job
    coin = job.context.split(" ")[1]
    id = job.context.split(" ")[0]
    context.bot.send_message(id, text=get_prices(Coins[coin]))


def set(update, context):
    chat_id = str(update.message.chat_id)
    coin = context.args[0].upper()
    context.job_queue.run_repeating(give, int(context.args[1]), context=chat_id + " " + coin)
