import requests
import json

symbol_list = requests.get('https://api.kucoin.com/api/v2/symbols').json()

aa = []

count = 0
not_count = 0

for get_all_info_symbol in symbol_list['data']:
    if get_all_info_symbol['enableTrading'] is True:
        count += 1
        aa.append(get_all_info_symbol)
    elif get_all_info_symbol['enableTrading'] is not True:
        not_count += 1

with open('../kucoin/1_25_step_1_pairs_trade.json', 'w') as file1:
    json.dump(aa, file1, indent=2)

print(f'Найдено и записано {count} монет.')
print(f'Не записано {not_count} монет.')
