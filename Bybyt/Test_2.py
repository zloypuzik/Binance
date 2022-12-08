import json

main_currency = 'USDT'

file_step_1_pairs_trade = 'step_1_pairs_trade.json'

def f_file_step_1_pairs_trade():
    with open(file_step_1_pairs_trade) as file_data:
        data_a = json.load(file_data)

    return data_a


all_pairs_usdt = []
all_pairs_not_usdt = []

pairs_buy_para_b = []
pairs_sell_para_b = []

pairs_buy_para_b_trade_usdt = []
pairs_sell_para_b_trade_usdt = []

buy_a_buy_b_sell_c = []
buy_a_sell_b_sell_c = []

# Если в общем словаре "file_step_1_pairs_trade" вторая валюта это "USDT", то добавляем пару в список "all_pairs_usdt"
for i in f_file_step_1_pairs_trade():
    if main_currency == (i['quoteCurrency']):
        symbol_a = (i['name'])
        baseAsset_a = (i['baseCurrency'])
        quoteAsset_a = (i['quoteCurrency'])
        all_pairs_usdt.append({'symbol_a': symbol_a, 'baseAsset_a': baseAsset_a, 'quoteAsset_a': quoteAsset_a})
# Если в общем списке "coin_para_a", и в первой паре , и во второй паре нет "USDT", то добавляем пару в список "para_b"
for ii in f_file_step_1_pairs_trade():
    if main_currency != (ii['quoteCurrency']):
        if main_currency != (ii['baseCurrency']):
            symbol_b = (ii['name'])
            baseAsset_b = (ii['baseCurrency'])
            quoteAsset_b = (ii['quoteCurrency'])
            all_pairs_not_usdt.append({'symbol_b': symbol_b, 'baseAsset_b': baseAsset_b, 'quoteAsset_b': quoteAsset_b})

for t in all_pairs_usdt:
    for tt in all_pairs_not_usdt:

        # Если покупаемая (базовая) валюта в списке 'all_pairs_usdt' равна котируемой валюте списка 'all_pairs_not_usdt'
        # то будем покупать базовую валюту из списка 'all_pairs_not_usdt' за котируемую валюту списка 'all_pairs_not_usdt'
        # например {'symbol_a': 'BTCUSDT', 'baseAsset': 'BTC', 'quoteAsset': 'USDT'} test2: {'symbol_b': 'NEOBTC', 'baseAsset': 'NEO', 'quoteAsset': 'BTC'}
        # тут мы покупаем "baseAsset': 'NEO'" за "quoteAsset': 'BTC'

        if t['baseAsset_a'] == tt['quoteAsset_b']:
            # print('buy', t['baseAsset'], t['quoteAsset'], tt['quoteAsset'],  tt)
            pairs_buy_para_b.append(
                {'symbol_b': tt['symbol_b'], 'baseAsset_b': tt['baseAsset_b'], 'quoteAsset_b': tt['quoteAsset_b']})
            continue

        # Если покупаемая (базовая) валюта в списке 'all_pairs_usdt' равна базовой валюте списка 'all_pairs_not_usdt'
        # то будем продавать базовую валюту из списка 'all_pairs_not_usdt' за котируемую валюту списка 'all_pairs_not_usdt'
        # например {'symbol_a': 'NEOUSDT', 'baseAsset': 'NEO', 'quoteAsset': 'USDT'} {'symbol_b': 'NEOBTC', 'baseAsset': 'NEO', 'quoteAsset': 'BTC'}
        # тут мы продаем "baseAsset': 'NEO'" и получаем "quoteAsset': 'BTC'"

        if t['baseAsset_a'] == tt['baseAsset_b']:
            # print('sell', t['baseAsset'], t['quoteAsset'], tt['baseAsset'], tt)
            pairs_sell_para_b.append(
                {'symbol_b': tt['symbol_b'], 'baseAsset_b': tt['baseAsset_b'], 'quoteAsset_b': tt['quoteAsset_b']})

#######################################################################################################################################################
# Проверяем что пары из списков "pairs_buy_para_b" и "pairs_sell_para_b" торгуются с USDT
#######################################################################################################################################################
for v in pairs_buy_para_b:
    for vv in all_pairs_usdt:
        if v['baseAsset_b'] == vv['baseAsset_a']:
            pairs_buy_para_b_trade_usdt.append(
                {'symbol_b': v['symbol_b'], 'baseAsset_b': v['baseAsset_b'], 'quoteAsset_b': v['quoteAsset_b']})
            break
for x in pairs_sell_para_b:
    for xx in all_pairs_usdt:
        if x['quoteAsset_b'] == xx['baseAsset_a']:
            pairs_sell_para_b_trade_usdt.append({'symbol_b': x['symbol_b'], 'baseAsset_b': x['baseAsset_b'], 'quoteAsset_b': x['quoteAsset_b']})
            break
#######################################################################################################################################################

for c in pairs_buy_para_b_trade_usdt:
    for cc in all_pairs_usdt:
        if c['baseAsset_b'] == cc['baseAsset_a']:
            buy_a_buy_b_sell_c.append({'symbol_a': cc['symbol_a'], 'symbol_b': c['symbol_b'], 'quoteAsset_b': c['quoteAsset_b']})
            break

test_buy_a_buy_b_sell_c = []

for b in buy_a_buy_b_sell_c:
    for bb in all_pairs_usdt:
        if b['quoteAsset_b'] == bb['baseAsset_a']:
            test_buy_a_buy_b_sell_c.append({'symbol_a': b['symbol_a'], 'symbol_b': b['symbol_b'], 'symbol_c': bb['symbol_a']})
            break
            #######################################################################################################################################################
for n in pairs_sell_para_b_trade_usdt:
    for nn in all_pairs_usdt:
        if n['quoteAsset_b'] == nn['baseAsset_a']:
            buy_a_sell_b_sell_c.append({'symbol_a': nn['symbol_a'], 'symbol_b': n['symbol_b'], 'quoteAsset_b': n['baseAsset_b']})
            break

test_buy_a_sell_b_sell_c = []

for m in buy_a_sell_b_sell_c:
    for mm in all_pairs_usdt:
        if m['quoteAsset_b'] == mm['baseAsset_a']:
            test_buy_a_sell_b_sell_c.append({'symbol_a': m['symbol_a'], 'symbol_b': m['symbol_b'], 'symbol_c': mm['symbol_a']})
            break
#######################################################################################################################################################

#for pp in test_buy_a_buy_b_sell_c:
   # print(pp)

with open('pairs_buy_para_b_trade_usdt.json', 'w') as file:
    json.dump(pairs_buy_para_b_trade_usdt, file, indent=2)

with open('pairs_sell_para_b_trade_usdt.json', 'w') as file1:
    json.dump(pairs_sell_para_b_trade_usdt, file1, indent=2)

with open('test_buy_a_buy_b_sell_c.json', 'w') as file2:
    json.dump(test_buy_a_buy_b_sell_c, file2, indent=2)

with open('test_buy_a_sell_b_sell_c.json', 'w') as file3:
    json.dump(test_buy_a_sell_b_sell_c, file3, indent=2)
