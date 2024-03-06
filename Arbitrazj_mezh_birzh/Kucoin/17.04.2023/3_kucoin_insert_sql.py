import requests
import json
import time
# get_currency_detail = requests.get('https://api.kucoin.com/api/v1/market/orderbook/level1?symbol=BTC-USDT').json()


##################################################################
kucoin_coin_info = '../Kucoin/symbol_list.json'


def f_file_binance_coin_info():
    with open(kucoin_coin_info) as file_data:
        data_a = json.load(file_data)

    return data_a
##################################################################
count = 0

test = []

start_time = time.time()  # Время начала работы функции
for i in f_file_binance_coin_info():
    if i['quoteCurrency'] == 'USDT':
        symbol = i['symbol']
        a = test.append(symbol)
        # print(symbol)
        # get_currency_detail = requests.get(f'https://api.kucoin.com/api/v2/currencies/{currency_symbol}').json()
        # get_orderbook = requests.get(f'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}').json()
        count += 1
        print(1)
        # print(symbol)
for ii in test:
    get_orderbook = requests.get(f'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={symbol}').json()
print('Затрачено на обработку', (time.time() - start_time), 'секунд.')
print(count)
