import json
import time
from binance.client import Client

api_key = "A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG"
secret_key = "zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA"

client = Client(
    api_key,
    secret_key
)

count_pairs_a = 0

tickers = client.get_all_tickers()
for test in tickers:
    print(test)
    count_pairs_a += 1
print(count_pairs_a)
aa = []

# for i in tickers:
#     get_symbol = i['symbol']
#     get_all_info_symbol = client.get_symbol_info(get_symbol)
#     if get_all_info_symbol is not None:
#         time.sleep(0.2)
#         status = get_all_info_symbol['status']
#         if status == 'TRADING':
#             aa.append(get_all_info_symbol)
#     else:
#         print("Нет пары:", get_symbol)
#
# with open('../Binance_BTC/1_25_step_1_pairs_trade2.json', 'w') as file1:
#     json.dump(aa, file1, indent=2)
