import json
import time
from datetime import datetime
from decimal import Decimal

from binance.client import Client as binance_client

########################################################################################################################


def apiBinance():

    apiKey = str("TZSHjpkEt8fEuquAaKU7rZaYIjYa2oO7xuJyAnzMZjPjVXsi74jCo76hFEtrOFFD")
    secretApiKey = str("HyDXw0T6WFq55ryrdZabmWDKnyUjAJPBxzFr310o50lNTYOHC2pdnUIO64pMBGBk")

    client = binance_client(
        apiKey,
        secretApiKey
    )

    return client

########################################################################################################################


def def_allMainCurrency(exchange):


    allMainCurrency = None

    match exchange:

        case "Binance":
            allMainCurrency = ['BUSD', 'USDT', 'BNB', 'BTC', 'ETH', 'XRP', 'TRX', 'DOGE', 'DOT', 'AUD', 'BIDR', 'BRL', 'EUR',
                               'GBR', 'RUB', 'TRY', 'DAI', 'UAH', 'ZAR', 'VAI', 'IDRT', 'NGN', 'PLN']

    return allMainCurrency