import requests
import json

# Получим по ссылки данные с ценами.
tickers = requests.get("https://api.huobi.pro/v2/settings/common/symbols").json()  # Получим ответ в виде JSON формата
# print(tickers)
# #
count_symbol = 0  # Счетчик торговых пар с ценами
aa = []

for i in tickers['data']:
    if i['state'] == 'online':
        print(i['p1'])

# print(f"Загрузил {count_symbol} торговых пар")