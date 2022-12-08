import time
import requests
import json
import time

# Получим по ссылки данные с ценами.
tickers = requests.get("https://api.huobi.pro/v2/settings/common/symbols").json()  # Получим ответ в виде JSON формата
# print(tickers)
# #
count_symbol = 0  # Счетчик торговых пар с ценами
aa = []

for i in tickers['data']:
    if i['state'] == 'online':
        count_symbol += 1
        aa.append(i)
    time.sleep(0.01)

print(f"Загрузил {count_symbol} торговых пар")

with open('../Huobi/1_25_step_1_pairs_trade222.json', 'w') as file1:
    json.dump(aa, file1, indent=2)
