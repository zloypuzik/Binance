import json
import requests

ain_currency = 'USDT'


file_step_1_pairs_trade = '../Huobi/1_25_step_1_pairs_trade222.json'


def f_file_step_1_pairs_trade():
    with open(file_step_1_pairs_trade) as file_data:
        data_a = json.load(file_data)

    return data_a

count_symbol = 0  # Счетчик торговых пар с ценами

all_pairs_usdt = []
all_pairs_b = []
pairs_buy_para_b = []

for i in f_file_step_1_pairs_trade():
    if (i['qcdn']) == "USDT":
        symbol_a = (i['sc'])
        baseAsset_a = (i['bcdn'])
        quoteAsset_a = (i['qcdn'])
        all_pairs_usdt.append({'symbol_a': symbol_a, 'baseAsset_a': baseAsset_a, 'quoteAsset_a': quoteAsset_a})

###########################################################################################
for i in all_pairs_usdt:
    bcdn = i['baseAsset_a']

    # para a [bcdn - AVAX] [qcdn - USDT] para b [bcdn - AVAX] [qcdn - ETH]
    # para a AVAX USDT para b AVAX USDC
    # para a AVAX USDT para b AVAX BTC
    for ii in f_file_step_1_pairs_trade():
        if bcdn == ii['bcdn'] and ii['bcdn'] != 'USDT' and ii['qcdn'] != 'USDT':
            symbol_b = (ii['sc'])
            baseAsset_b = (ii['bcdn'])
            quoteAsset_b = (ii['qcdn'])
            all_pairs_b.append({'symbol_b': symbol_b, 'baseAsset_b': baseAsset_b, 'quoteAsset_b': quoteAsset_b})
            #count_symbol += 1

for t in all_pairs_usdt:
    for tt in all_pairs_b:
        if t['baseAsset_a'] == tt['baseAsset_b']:
            pairs_buy_para_b.append(
                {'symbol_a': t['symbol_a'], 'baseAsset_a': t['baseAsset_a'], 'quoteAsset_a': t['quoteAsset_a'], 'symbol_b': tt['symbol_b'], 'baseAsset_b': tt['baseAsset_b'],
                 'quoteAsset_b': tt['quoteAsset_b'], 'symbol_c': tt['quoteAsset_b'] + t['quoteAsset_a'], 'baseAsset_c': tt['quoteAsset_b'], 'quoteAsset_c': t['quoteAsset_a']})
            print(tt['quoteAsset_b'])


            break

###########################################################################################

# for i in pairs_buy_para_b:
#     qcdn = i['qcdn']
#     #print(qcdn)
#
#     for ii in f_file_step_1_pairs_trade():
#         if qcdn == ii['bcdn']:
#             print(ii)
    # print("para a", i['bcdn'], i['qcdn'])

#print(f"Загрузил {count_symbol} торговых пар")
            #print("para a", i['bcdn'], i['qcdn'], "para b", ii['bcdn'], ii['qcdn'])
    # for iii in f_file_step_1_pairs_trade():
    #     if bcdn == iii['qcdn'] and iii['bcdn'] != 'USDT' and iii['qcdn'] != 'USDT':
    #         # pairs_buy_para_b.append(ii)
    #         print("para a", i['bcdn'], i['qcdn'], "para b", iii['bcdn'], iii['qcdn'])

#print(f"Загрузил {count_symbol} торговых пар")
#print(type(all_pairs_usdt))
with open('../Huobi/1_pairs_buy_para_b_test.json', 'w') as file3:
    json.dump(pairs_buy_para_b, file3, indent=2)