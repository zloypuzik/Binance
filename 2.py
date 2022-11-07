import json
from binance.client import Client

api_key = "A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG"
secret_key = "zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA"

client = Client(
    api_key,
    secret_key
)

main_currency = 'USDT'

tickers = client.get_all_tickers()

file_step_1_pairs_trade = '1_25_step_1_pairs_trade.json'


# file_step_1_pairs_trade = 'para_aa.json'


def f_file_step_1_pairs_trade():
    with open(file_step_1_pairs_trade) as file_data:
        data_a = json.load(file_data)

    return data_a


all_pairs_usdt = []
all_pairs_btc = []
all_pairs_not_usdt = []

pairs_buy_para_b = []
pairs_sell_para_b = []

pairs_buy_para_b_trade_usdt = []
pairs_sell_para_b_trade_usdt = []

buy_a_buy_b_sell_c = []
buy_a_sell_b_sell_c = []

# Если в общем словаре "file_step_1_pairs_trade" вторая валюта это "USDT" или "BTC", то добавляем пару в список
# "all_pairs_usdt"
for i in f_file_step_1_pairs_trade():
    if (i['quoteAsset']) == "USDT":
        symbol_a = (i['symbol'])
        baseAsset_a = (i['baseAsset'])
        quoteAsset_a = (i['quoteAsset'])
        stepSize_a = (i['filters'][2]['stepSize'])
        all_pairs_usdt.append(
            {'symbol_a': symbol_a, 'baseAsset_a': baseAsset_a, 'quoteAsset_a': quoteAsset_a, 'stepSize_a': stepSize_a})
        # print(symbol_a, stepSize_a)

for ii in f_file_step_1_pairs_trade():
    if (ii['quoteAsset']) == "BTC":
        symbol_b = (ii['symbol'])
        baseAsset_b = (ii['baseAsset'])
        quoteAsset_b = (ii['quoteAsset'])
        stepSize_b = (ii['filters'][2]['stepSize'])
        all_pairs_btc.append(
            {'symbol_b': symbol_b, 'baseAsset_b': baseAsset_b, 'quoteAsset_b': quoteAsset_b, 'stepSize_b': stepSize_b})

for t in all_pairs_usdt:
    for tt in all_pairs_btc:
        if t['baseAsset_a'] == tt['baseAsset_b']:
            pairs_buy_para_b.append(
                {'symbol_a': t['symbol_a'], 'baseAsset_a': t['baseAsset_a'], 'quoteAsset_a': t['quoteAsset_a'],
                 'stepSize_a': t['stepSize_a'], 'symbol_b': tt['symbol_b'], 'baseAsset_b': tt['baseAsset_b'],
                 'quoteAsset_b': tt['quoteAsset_b'], 'stepSize_b': tt['stepSize_b']})

            break

with open('1_pairs_buy_para_b_test.json', 'w') as file3:
    json.dump(pairs_buy_para_b, file3, indent=2)
