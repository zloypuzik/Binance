import json
import requests
from kucoin.client import Client

api_key = '63cc9d027675230001bba629'
api_secret = '0e8444e7-0594-4a57-a058-92d34decd0d7'

client = Client(api_key, api_secret, passphrase='4796212')

a = client.get_ticker()
print(a)
#
# for i in a['ticker']:
#     print(i)
# print(a['ticker'])

# print(a['ticker'][0]['symbol'], a['ticker'][0]['buy'], a['ticker'][0]['sell'])

# get_currency_detail = requests.get('https://api.kucoin.com/api/v2/currencies/BTC').json()
# get_currency_detail = requests.get('https://api.kucoin.com/api/v3/market/orderbook/level2').json()
# print(get_currency_detail)

# aa = []
#
# for get_all_info_symbol in get_currency_detail['data']:
#     if get_all_info_symbol['enableTrading'] is True:
#         aa.append(get_all_info_symbol)
#
# with open('../Kucoin/symbol_list.json', 'w') as file1:
#     json.dump(aa, file1, indent=2)