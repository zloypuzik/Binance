import time
import requests
import json

# Получим по ссылки данные с ценами.
tickers = requests.get("https://api.huobi.pro/v1/settings/common/market-symbols").json()  # Получим ответ в виде JSON формата
# print(tickers)
# #
count_symbol = 0  # Счетчик торговых пар с ценами
aa = []

#print(tickers)

for i in tickers['data']:
    if i['symbol'] == 'btcusdt':
        #@count_symbol += 1
        aa.append(i)
        #print(i)

# print(f"Загрузил {count_symbol} торговых пар")
#
with open('../Huobi/1_25_step_1_pairs_trade333.json', 'w') as file1:
    json.dump(aa, file1, indent=2)
