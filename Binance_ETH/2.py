import json

########################################################################################################

file_step_1_pairs_trade = '../Binance_ETH/1_25_step_1_pairs_trade.json'

def f_file_step_1_pairs_trade():
    with open(file_step_1_pairs_trade) as file_data:
        data_a = json.load(file_data)

    return data_a

########################################################################################################

main_currency = 'ETH'

all_pairs_c = ['BUSD', 'USDT', 'BNB', 'BTC', 'ETH', 'XRP', 'TRX', 'DOGE', 'DOT', 'AUD', 'BIDR', 'BRL', 'EUR', 'GBR', 'RUB', 'TRY', 'DAI', 'UAH', 'ZAR', 'VAI', 'IDRT', 'NGN', 'PLN']  # Валюта, за которую можно купить или продать другую валюту.

########################################################################################################
# Проверяем кем является 'main_currency' относительно других основных монет
########################################################################################################

main_currency_quoteAsset_b = []
quoteAsset_b_main_currency = []

for test in f_file_step_1_pairs_trade():
    if test['baseAsset'] == main_currency:
        main_currency_quoteAsset_b.append(test['quoteAsset'])

# Пример: ETH/UAH


for test2 in f_file_step_1_pairs_trade():
    if test2['quoteAsset'] == main_currency:
        for test22 in all_pairs_c:
            if test2['baseAsset'] == test22:
                quoteAsset_b_main_currency.append(test2['baseAsset'])

# Пример: BNB/ETH

########################################################################################################
# Если в общем словаре "file_step_1_pairs_trade" вторая валюта это 'main_currency', то добавляем пару в список 'all_pairs_a'
########################################################################################################

count_pairs_a = 0
all_pairs_a = []

for i in f_file_step_1_pairs_trade():
    if (i['quoteAsset']) == main_currency:
        symbol_a = (i['symbol'])
        baseAsset_a = (i['baseAsset'])
        quoteAsset_a = (i['quoteAsset'])
        stepSize_a = (i['filters'][1]['stepSize'])
        all_pairs_a.append(
            {'symbol_a': symbol_a, 'baseAsset_a': baseAsset_a, 'quoteAsset_a': quoteAsset_a, 'stepSize_a': stepSize_a})
        count_pairs_a += 1

print('Найдено:', count_pairs_a, 'валют,', 'торгуемые с', main_currency)


########################################################################################################
# Ищем все пары которые торгуются с 'main_currency' (из первого круга) и добавляем пару в список 'all_pairs_b'
########################################################################################################

count_pairs_b = 0
all_pairs_b = []


for ii in f_file_step_1_pairs_trade():
    for iii in all_pairs_a:
        if (iii['baseAsset_a']) == (ii['baseAsset']) and (ii['quoteAsset'] != main_currency):
            symbol_b = (ii['symbol'])
            baseAsset_b = (ii['baseAsset'])
            quoteAsset_b = (ii['quoteAsset'])
            stepSize_b = (ii['filters'][1]['stepSize'])
            all_pairs_b.append(
                {'symbol_b': symbol_b, 'baseAsset_b': baseAsset_b, 'quoteAsset_b': quoteAsset_b, 'stepSize_b': stepSize_b})
            count_pairs_b += 1

print('Найдено:', count_pairs_b, 'возможных пар, для торговли второго круга')

########################################################################################################



count_pairs_c = 0
pairs_buy_para_b = []

for t in all_pairs_a:
    for tt in all_pairs_b:
        if t['baseAsset_a'] == tt['baseAsset_b']:



            pairs_buy_para_b.append(
                {'symbol_a': t['symbol_a'], 'baseAsset_a': t['baseAsset_a'], 'quoteAsset_a': t['quoteAsset_a'],
                 'stepSize_a': t['stepSize_a'], 'symbol_b': tt['symbol_b'], 'baseAsset_b': tt['baseAsset_b'],
                 'quoteAsset_b': tt['quoteAsset_b'], 'stepSize_b': tt['stepSize_b']})
            count_pairs_c += 1

# for t in all_pairs_a:
#     for tt in all_pairs_b:
#         if t['baseAsset_a'] == tt['baseAsset_b']:
#             pairs_buy_para_b.append(
#                 {'symbol_a': t['symbol_a'], 'baseAsset_a': t['baseAsset_a'], 'quoteAsset_a': t['quoteAsset_a'],
#                  'stepSize_a': t['stepSize_a'], 'symbol_b': tt['symbol_b'], 'baseAsset_b': tt['baseAsset_b'],
#                  'quoteAsset_b': tt['quoteAsset_b'], 'stepSize_b': tt['stepSize_b']})
#             count_pairs_c += 1

print(count_pairs_c)
#print(pairs_buy_para_b)
# for test in pairs_buy_para_b:
#     print(test)

# for test2 in f_file_step_1_pairs_trade():
#     for test22 in pairs_buy_para_b:
#         if test2['baseAsset'] == test22['quoteAsset_b']:
#             print(test2['symbol'])
#         else:
#             print('###############', test2['symbol'])

with open('1_pairs_buy_para_b_test.json', 'w') as file3:
    json.dump(pairs_buy_para_b, file3, indent=2)
