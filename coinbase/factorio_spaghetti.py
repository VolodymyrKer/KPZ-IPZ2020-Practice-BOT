from datetime import datetime

import requests

from settings.enum_coins import Coins


def get_prices(coin: Coins):
    response_sell = requests.get(f"https://api.coinbase.com/v2/prices/{coin.value[0]}/sell")
    response_spot = requests.get(f"https://api.coinbase.com/v2/prices/{coin.value[0]}/spot")
    response_buy = requests.get(f"https://api.coinbase.com/v2/prices/{coin.value[0]}/buy")
    data_sell = response_sell.json()
    data_spot = response_spot.json()
    data_buy = response_buy.json()
    result = f"---  {coin.value[0]}  ---\n" \
             f"Time: {datetime.strftime(datetime.now(),'%d.%m.%Y %H:%M:%S')}\n" \
             f"Sell: {data_sell.get('data').get('amount')} {data_sell.get('data').get('currency')}\n" \
             f"Buy: {data_buy.get('data').get('amount')} {data_buy.get('data').get('currency')}\n" \
             f"Spot: {round(float(data_spot.get('data').get('amount')), 2)} {data_spot.get('data').get('currency')}\n"
    return result
